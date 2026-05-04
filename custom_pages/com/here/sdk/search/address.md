---
title: "Address (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestaddress"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Address

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.Address
------------------------------------------------------------------------
public final class Address extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Information about the address of a location.

Used in [`Place.getAddress()`](sdk-for-android-explore-api-reference-latestplace#getAddress()).

Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only [`addressText`](#addressText). Complete address details can be obtained by searching with [`PlaceIdQuery`](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search").

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [addressText](#addressText)

The text for the address, for example, "Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [block](#block)

The block number for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [city](#city)

The city name for the address, for example, "Brooklyn".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [country](#country)

The country name for the address, for example, "United States".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [countryCode](#countryCode)

An ISO-3166-1 (3-letter) country code for the address, for example, "USA".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [county](#county)

The county name for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [district](#district)

The district name for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [houseNumOrName](#houseNumOrName)

The house name or number for the address, for example, "347".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [postalCode](#postalCode)

The postal code for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [state](#state)

The state name for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [stateCode](#stateCode)

The state code for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [street](#street)

The street name for the address, for example, "Lewis Ave".

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [subBlock](#subBlock)

The sub-block number for the address.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [subdistrict](#subdistrict)

The subdistrict name for the address.

[`AddressType`](sdk-for-android-explore-api-reference-latestaddresstype "enum class in com.here.sdk.search")

  [type](#type)

Specifies the address type.

## Constructor Summary

Constructors

Constructor

  Description

  [Address](#%3Cinit%3E())`()`

Default constructor.

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

### city

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) city

    The city name for the address, for example, "Brooklyn". Note: This String can be empty when no data is available.

### countryCode

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) countryCode

    An ISO-3166-1 (3-letter) country code for the address, for example, "USA". Note: This String can be empty when no data is available.

### country

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) country

    The country name for the address, for example, "United States". Note: This String can be empty when no data is available.

### district

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) district

    The district name for the address. It is a division of city, typically an administrative unit within a larger city or a customary name of a city's neighborhood, for example, "Bedford-Stuyvesant". Note: This String can be empty when no data is available.

### subdistrict

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) subdistrict

    The subdistrict name for the address. It is a subdivision of a district. Note: This String can be empty when no data is available.

### houseNumOrName

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) houseNumOrName

    The house name or number for the address, for example, "347". Note: This String can be empty when no data is available.

### postalCode

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) postalCode

    The postal code for the address. It is an alphanumeric string included in a postal address to facilitate mail sorting, known locally in various countries throughout the world as a postcode, post code, PIN or ZIP Code, for example, "11233". Note: This String can be empty when no data is available.

### state

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) state

    The state name for the address. It is the name of the state division of a country, for example, "New York". Note: This String can be empty when no data is available.

### county

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) county

    The county name for the address. It is a division of a state, typically a secondary-level administrative division of a country or equivalent, for example, "Kings". Note: This String can be empty when no data is available.

### street

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) street

    The street name for the address, for example, "Lewis Ave". Note: This String can be empty when no data is available.

### block

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) block

    The block number for the address. It is part of Japanese addressing system. Note: This String can be empty when no data is available.

### subBlock

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) subBlock

    The sub-block number for the address. It is part of Japanese addressing system. Note: This String can be empty when no data is available.

### addressText

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) addressText

    The text for the address, for example, "Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States". Note: This String can be empty when no data is available.

### type

@Nullable public [AddressType](sdk-for-android-explore-api-reference-latestaddresstype "enum class in com.here.sdk.search") type

    Specifies the address type.

### stateCode

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stateCode

    The state code for the address. It is code/abbreviation of the state division of a country, for example, "NY". Note: This String can be empty when no data is available.

## Constructor Details

  - ()" class="section detail">

### Address

public Address()

    Default constructor. Note: Sets all the string values to "".

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
