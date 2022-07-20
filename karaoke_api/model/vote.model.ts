import { Table, Column, Model } from 'sequelize-typescript'

@Table
export class Vote extends Model {

  @Column
  song_id: number

  @Column
  date: Date

}