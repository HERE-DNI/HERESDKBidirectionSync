---
title: "LocalizedText (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocalizedtext"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LocalizedText

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.LocalizedText
------------------------------------------------------------------------
public final class LocalizedText extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Used to represent text localized to specific language.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html)

  [locale](#locale)

Locale of text, in most cases contains only language code.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [text](#text)

Text value.

## Constructor Summary

Constructors

Constructor

  Description

  [LocalizedText](#%3Cinit%3E(java.lang.String,java.util.Locale))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` text, `[Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html)` locale)`

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

### text

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text

    Text value.

### locale

@Nullable public [Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html) locale

    Locale of text, in most cases contains only language code. If locale is not supported by the platform, `null` is returned.

## Constructor Details

  - (java.lang.String,java.util.Locale)" class="section detail">

### LocalizedText

public LocalizedText(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text, @Nullable [Locale](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Locale.html) locale)

    Creates a new instance.
Parameters:
    `text` -

    Text value.

    `locale` -

    Locale of text, in most cases contains only language code. If locale is not supported by the platform, `null` is returned.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
