---
title: "CategoryQuery (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcategoryquery"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CategoryQuery

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.CategoryQuery
------------------------------------------------------------------------
public final class CategoryQuery extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify a query by categories.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area)

Area to perform search on.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`CategoryQuery.Area`](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search")

  [area](#area)

Area in which to provide the most relevant places.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [categories](#categories)

List of categories to be included.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`>`

  [excludeCategories](#excludeCategories)

List of categories and subcategories to be excluded.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceChain`](sdk-for-android-explore-api-reference-latestplacechain "class in com.here.sdk.search")`>`

  [excludeChains](#excludeChains)

List of chains to be excluded.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceFoodType`](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")`>`

  [excludeFoodTypes](#excludeFoodTypes)

List of food types to be excluded.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [filter](#filter)

Full-text filter on POI names/titles.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceChain`](sdk-for-android-explore-api-reference-latestplacechain "class in com.here.sdk.search")`>`

  [includeChains](#includeChains)

List of chains to be included.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceFoodType`](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")`>`

  [includeFoodTypes](#includeFoodTypes)

List of food types to be included.

[`PlaceFilter`](sdk-for-android-explore-api-reference-latestplacefilter "class in com.here.sdk.search")

  [placeFilter](#placeFilter)

The filter options to specify a place in query.

## Constructor Summary

Constructors

Constructor

  Description

  [CategoryQuery](#%3Cinit%3E(com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area))`(`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")` category, `[`CategoryQuery.Area`](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search")` area)`

Constructs a new instance of this class from provided parameters.

[CategoryQuery](#%3Cinit%3E(com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area))`(`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")` category, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` filter, `[`CategoryQuery.Area`](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search")` area)`

Constructs a new instance of this class from provided parameters.

[CategoryQuery](#%3Cinit%3E(java.util.List,com.here.sdk.search.CategoryQuery.Area))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[`CategoryQuery.Area`](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search")` area)`

Constructs a new instance of this class from provided parameters.

[CategoryQuery](#%3Cinit%3E(java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PlaceCategory`](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")`> categories, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` filter, `[`CategoryQuery.Area`](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search")` area)`

Constructs a new instance of this class from provided parameters.

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

### categories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories

    List of categories to be included. A place can be assigned multiple categories. If any of them is in `CategoryQuery.categories`, but none are in `CategoryQuery.excludeCategories`, that place will be included in the response.

### excludeCategories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> excludeCategories

    List of categories and subcategories to be excluded. A place can be assigned multiple categories. If any of them is in `CategoryQuery.excludeCategories`, that place will not be included in the response, regardless of whether any of its assigned categories have been included in `CategoryQuery.categories`. In short, an exclusion will always win over an inclusion. This is especially useful for excluding specific subcategories from the main category.

### includeChains

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceChain](sdk-for-android-explore-api-reference-latestplacechain "class in com.here.sdk.search")\> includeChains

    List of chains to be included. A place can be assigned multiple chains. If any of them is in `CategoryQuery.includeChains`, but none are in `CategoryQuery.excludeChains`, that place will be included in the response.

### excludeChains

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceChain](sdk-for-android-explore-api-reference-latestplacechain "class in com.here.sdk.search")\> excludeChains

    List of chains to be excluded. A place can be assigned multiple chains. If any of them is in `CategoryQuery.excludeChains`, that place will not be included in the response, regardless of whether any of its assigned chains have been included in `CategoryQuery.includeChains`. In short, an exclusion will always win over an inclusion.

### includeFoodTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceFoodType](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")\> includeFoodTypes

    List of food types to be included. A place can be assigned multiple food types. If any of them is in `CategoryQuery.includeFoodTypes`, but none are in `CategoryQuery.excludeFoodTypes`, that place will be included in the response.

### excludeFoodTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceFoodType](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")\> excludeFoodTypes

    List of food types to be excluded. A place can be assigned multiple food types. If any of them is in `CategoryQuery.excludeFoodTypes`, that place will not be included in the response, regardless of whether any of its assigned food types have been included in `CategoryQuery.includeFoodTypes`. In short, an exclusion will always win over an inclusion.

### filter

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filter

    Full-text filter on POI names/titles. Results with a partial match are included in the response. By default the value is set to null and results will be based on other parameters provided.

### placeFilter

@NonNull public [PlaceFilter](sdk-for-android-explore-api-reference-latestplacefilter "class in com.here.sdk.search") placeFilter

    The filter options to specify a place in query. Consists of fuel and truck options.

### area

@NonNull public [CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search") area

    Area in which to provide the most relevant places.

## Constructor Details

  - (com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area)" class="section detail">

### CategoryQuery

public CategoryQuery(@NonNull [PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search") category, @NonNull [CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search") area)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `category` -

    Category for query

    `area` -

    Area in which to provide the most relevant places.
- (java.util.List,com.here.sdk.search.CategoryQuery.Area)" class="section detail">

### CategoryQuery

public CategoryQuery(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search") area)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `categories` -

    List of categories.

    `area` -

    Area in which to provide the most relevant places.
- (com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area)" class="section detail">

### CategoryQuery

public CategoryQuery(@NonNull [PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search") category, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filter, @NonNull [CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search") area)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `category` -

    Category for query

    `filter` -

    Full-text filter on POI names/titles. Results with a partial match are included in the response.

    `area` -

    Area in which to provide the most relevant places.
- (java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area)" class="section detail">

### CategoryQuery

public CategoryQuery(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")\> categories, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filter, @NonNull [CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search") area)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `categories` -

    List of categories.

    `filter` -

    Full-text filter on POI names/titles. Results with a partial match are included in the response.

    `area` -

    Area in which to provide the most relevant places.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
