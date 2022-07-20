import { APILogger } from '../logger/api.logger';
import { KaraokeService } from '../service/karaoke.service';

export class KaraokeController {

    private KaraokeService: KaraokeService;
    private logger: APILogger;

    constructor() {
        this.KaraokeService = new KaraokeService();
        this.logger = new APILogger()
    }

    async getSongs() {
        this.logger.info('Controller: getSongs', "started")
        return await this.KaraokeService.getSongs();
    }

    async voteSong(song) {
        this.logger.info('Controller: voteSong', song);
        return await this.KaraokeService.voteSong(song);
    }
}