import { KaraokeRepository } from '../repository/karaoke.repository';

export class KaraokeService {

    private KaraokeRepository: KaraokeRepository;

    constructor() {
        this.KaraokeRepository = new KaraokeRepository();
    }

    async getSongs() {
        return await this.KaraokeRepository.getSongs();
    }

    async voteSong(Song) {
        return await this.KaraokeRepository.voteSong(Song);
    }

}