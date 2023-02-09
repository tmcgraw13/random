package com.backend.mysqldata;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity // This tells Hibernate to make a table out of this class
public class User {
  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Integer personId;

  private String username;

  public Integer getId() {
    return personId;
  }

  public void setId(Integer id) {
    this.personId = id;
  }

  public String getName() {
    return username;
  }

  public void setName(String name) {
    this.username = name;
  }

}