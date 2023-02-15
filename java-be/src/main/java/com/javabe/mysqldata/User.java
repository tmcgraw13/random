package com.javabe.mysqldata;

import com.fasterxml.jackson.annotation.JsonProperty;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name="user_tbl")
public class User {

  @Id
  @GeneratedValue(strategy=GenerationType.IDENTITY)
  private Long personid;

  @JsonProperty("name")
  String username;


  public Long getId() {
    return personid;
  }

  public void setId(Long id) {
    this.personid = id;
  }

  public String getName() {
    return username;
  }

  public void setName(String name) {
    this.username = name;
  }

}