import { Table, Column, Model, HasMany } from 'sequelize-typescript'

@Table
export class Song extends Model {

  @Column
  name: string

  @Column
  singer: string

  @Column
  year: string

  @Column
  genre: string

  @Column
  count?: number

}