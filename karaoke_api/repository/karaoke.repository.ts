import { connect } from "../config/db.config";
import { APILogger } from '../logger/api.logger';
import { Song } from "../model/song.model";
import { Vote } from "../model/vote.model";

let voters: Array<string> = [];

export class KaraokeRepository {

    private logger: APILogger;
    private db: any = {};
    private KaraokeRespository: any;
    private VoteRespository: any;

    constructor() {
        this.db = connect();
        // For Development
        this.db.sequelize.sync().then(() => {
            console.log("Drop and re-sync db.");
        });
        this.db.sequelize
        .authenticate()
        .then(() => {
            console.log('Connection has been established successfully.');
        })
        .catch(err => {
            console.error('Unable to connect to the database:', err);
        });
        this.KaraokeRespository = this.db.sequelize.getRepository(Song);
        this.VoteRespository = this.db.sequelize.getRepository(Vote);

    }

    async getSongs() {

        try {
            let data: Array<Song> = await this.KaraokeRespository.findAll();
            // FIX SCORES
            // one week
            const max_date = 7*24*60*60*1000;
            const now = new Date();

            for(let s of data){
                let count:number = 0
                let votes: Array<Vote> = await this.VoteRespository.findAll({
                    where: {
                        song_id: s.id
                      }                
                });
                if(s.name == null){
                        continue;
                }
                for(let v of votes){
                    let timeDiffInMs = now.getTime() - v.date.getTime();
                    let value = 2;
                    if(timeDiffInMs >= max_date){
                        value = 1;
                    }
                    count+= value;
                }
                s.count = count;
            }
            // Descending order
            let dataSorted = data.sort((a, b) => (a.count > b.count) ? -1 : 1);

            console.log('Songs:::', data);
            return {dataSorted};
        } catch (err) {
            console.log(err);
            return [];
        }
    }

    async voteSong(song:Song) {
        let data:Song;
        let v:Vote;
        try {

            const dateTime = new Date();

            const s: Array<Song> = await this.KaraokeRespository.findAll({
                name: song.name,
                genre: song.genre,
                year: song.year,
                singer: song.singer
            });

            if(s.length == 0){

                song.count = 2;
                // Add date timestamp and count

                data = await this.KaraokeRespository.create(song);

                let vote = {song_id:data.id, date:dateTime};
                v = await this.VoteRespository.create(vote);

            }
            else{
                for(let sing of s){
                    if(sing.name == null){
                        continue;
                    }
                    sing.count += 2;
                    // save vote as well and link to song
                    let vote = {song_id:sing.id, date:dateTime};
                    v = await this.VoteRespository.create(vote);                }
            }

        } catch(err) {
            this.logger.error('Error::' + err);
        }
        return v;
    }

}