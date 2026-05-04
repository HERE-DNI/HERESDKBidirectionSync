---
title: "WebEditorial (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestwebeditorial"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class WebEditorial

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.WebEditorial
------------------------------------------------------------------------
public final class WebEditorial extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains information about editorial article and a link to it.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [description](#description)

Content of the editorial.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [language](#language)

Information about language in which edtitorial was written.

[`WebSource`](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")

  [source](#source)

Detailed information about editorial article.

## Constructor Summary

Constructors

Constructor

  Description

  [WebEditorial](#%3Cinit%3E())`()`

Creates a new instance.

[WebEditorial](#%3Cinit%3E(java.lang.String,java.lang.String,com.here.sdk.search.WebSource))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` description, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` language, `[`WebSource`](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")` source)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### description

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description

    Content of the editorial.

### language

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) language

    Information about language in which edtitorial was written.

### source

@NonNull public [WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search") source

    Detailed information about editorial article.

## Constructor Details

  - (java.lang.String,java.lang.String,com.here.sdk.search.WebSource)" class="section detail">

### WebEditorial

public WebEditorial(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) language, @NonNull [WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search") source)

    Creates a new instance.
Parameters:
    `description` -

    Content of the editorial.

    `language` -

    Information about language in which edtitorial was written.

    `source` -

    Detailed information about editorial article.
- ()" class="section detail">

### WebEditorial

public WebEditorial()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
