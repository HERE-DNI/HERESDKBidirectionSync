---
title: "Contact (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcontact"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Contact

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.Contact
------------------------------------------------------------------------
public final class Contact extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents contact information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EmailAddress`](sdk-for-android-explore-api-reference-latestemailaddress "class in com.here.sdk.search")`>`

  [emails](#emails)

The list of email addresses with associated categories.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LandlinePhone`](sdk-for-android-explore-api-reference-latestlandlinephone "class in com.here.sdk.search")`>`

  [landlinePhones](#landlinePhones)

The list of landline phone numbers with associated categories.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MobilePhone`](sdk-for-android-explore-api-reference-latestmobilephone "class in com.here.sdk.search")`>`

  [mobilePhones](#mobilePhones)

The list of mobile phones numbers with associated categories.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebsiteAddress`](sdk-for-android-explore-api-reference-latestwebsiteaddress "class in com.here.sdk.search")`>`

  [websites](#websites)

The list of website addresses with associated categories.

## Constructor Summary

Constructors

Constructor

  Description

  [Contact](#%3Cinit%3E())`()`

Creates a new instance.

[Contact](#%3Cinit%3E(java.util.List,java.util.List,java.util.List,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LandlinePhone`](sdk-for-android-explore-api-reference-latestlandlinephone "class in com.here.sdk.search")`> landlinePhones, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MobilePhone`](sdk-for-android-explore-api-reference-latestmobilephone "class in com.here.sdk.search")`> mobilePhones, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`EmailAddress`](sdk-for-android-explore-api-reference-latestemailaddress "class in com.here.sdk.search")`> emails, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WebsiteAddress`](sdk-for-android-explore-api-reference-latestwebsiteaddress "class in com.here.sdk.search")`> websites)`

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

### landlinePhones

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LandlinePhone](sdk-for-android-explore-api-reference-latestlandlinephone "class in com.here.sdk.search")\> landlinePhones

    The list of landline phone numbers with associated categories. This data is not available in offline search.

### mobilePhones

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MobilePhone](sdk-for-android-explore-api-reference-latestmobilephone "class in com.here.sdk.search")\> mobilePhones

    The list of mobile phones numbers with associated categories. This data is not available in offline search.

### emails

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EmailAddress](sdk-for-android-explore-api-reference-latestemailaddress "class in com.here.sdk.search")\> emails

    The list of email addresses with associated categories. This data is not available in offline search.

### websites

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebsiteAddress](sdk-for-android-explore-api-reference-latestwebsiteaddress "class in com.here.sdk.search")\> websites

    The list of website addresses with associated categories. This data is not available in offline search.

## Constructor Details

  - ()" class="section detail">

### Contact

public Contact()

    Creates a new instance.

  - (java.util.List,java.util.List,java.util.List,java.util.List)" class="section detail">

### Contact

public Contact(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LandlinePhone](sdk-for-android-explore-api-reference-latestlandlinephone "class in com.here.sdk.search")\> landlinePhones, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MobilePhone](sdk-for-android-explore-api-reference-latestmobilephone "class in com.here.sdk.search")\> mobilePhones, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[EmailAddress](sdk-for-android-explore-api-reference-latestemailaddress "class in com.here.sdk.search")\> emails, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WebsiteAddress](sdk-for-android-explore-api-reference-latestwebsiteaddress "class in com.here.sdk.search")\> websites)

    Creates a new instance.
Parameters:
    `landlinePhones` -

    The list of landline phone numbers with associated categories. This data is not available in offline search.

    `mobilePhones` -

    The list of mobile phones numbers with associated categories. This data is not available in offline search.

    `emails` -

    The list of email addresses with associated categories. This data is not available in offline search.

    `websites` -

    The list of website addresses with associated categories. This data is not available in offline search.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
