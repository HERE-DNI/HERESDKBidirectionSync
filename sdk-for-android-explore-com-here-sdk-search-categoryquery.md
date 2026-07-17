---
title: "CategoryQuery (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-categoryquery"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.search.CategoryQuery → com.here.sdk.search.CategoryQuery

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">CategoryQuery</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify a query by categories.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" class="type-name-link" title="class in com.here.sdk.search"><code>CategoryQuery.Area</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Area to perform search on.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">`CategoryQuery.Area`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#area" class="member-name-link"><code>area</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Area in which to provide the most relevant places.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">`PlaceCategory`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#categories" class="member-name-link"><code>categories</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of categories to be included.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">`PlaceCategory`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#excludeCategories" class="member-name-link"><code>excludeCategories</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of categories and subcategories to be excluded.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-search-placechain" title="class in com.here.sdk.search">`PlaceChain`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#excludeChains" class="member-name-link"><code>excludeChains</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of chains to be excluded.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">`PlaceFoodType`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#excludeFoodTypes" class="member-name-link"><code>excludeFoodTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of food types to be excluded.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#filter" class="member-name-link"><code>filter</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Full-text filter on POI names/titles.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-search-placechain" title="class in com.here.sdk.search">`PlaceChain`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#includeChains" class="member-name-link"><code>includeChains</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of chains to be included.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">`PlaceFoodType`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#includeFoodTypes" class="member-name-link"><code>includeFoodTypes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of food types to be included.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-placefilter" title="class in com.here.sdk.search">`PlaceFilter`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery#placeFilter" class="member-name-link"><code>placeFilter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The filter options to specify a place in query.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      CategoryQuery ( PlaceCategory category, CategoryQuery.Area area)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      CategoryQuery ( PlaceCategory category, String filter, CategoryQuery.Area area)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      CategoryQuery ( List < PlaceCategory > categories, CategoryQuery.Area area)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      CategoryQuery ( List < PlaceCategory > categories, String filter, CategoryQuery.Area area)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-categories" class="section detail">

    ### categories

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>\></span> <span class="element-name">categories</span>

    </div>

    <div class="block">

    List of categories to be included. A place can be assigned multiple categories. If any of them is in CategoryQuery.categories , but none are in CategoryQuery.excludeCategories , that place will be included in the response.

    </div>

    </div>

  - <div id="sdk-for-android-explore-excludeCategories" class="section detail">

    ### excludeCategories

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>\></span> <span class="element-name">excludeCategories</span>

    </div>

    <div class="block">

    List of categories and subcategories to be excluded. A place can be assigned multiple categories. If any of them is in CategoryQuery.excludeCategories , that place will not be included in the response, regardless of whether any of its assigned categories have been included in CategoryQuery.categories . In short, an exclusion will always win over an inclusion. This is especially useful for excluding specific subcategories from the main category.

    </div>

    </div>

  - <div id="sdk-for-android-explore-includeChains" class="section detail">

    ### includeChains

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placechain" title="class in com.here.sdk.search">PlaceChain</a>\></span> <span class="element-name">includeChains</span>

    </div>

    <div class="block">

    List of chains to be included. A place can be assigned multiple chains. If any of them is in CategoryQuery.includeChains , but none are in CategoryQuery.excludeChains , that place will be included in the response.

    </div>

    </div>

  - <div id="sdk-for-android-explore-excludeChains" class="section detail">

    ### excludeChains

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placechain" title="class in com.here.sdk.search">PlaceChain</a>\></span> <span class="element-name">excludeChains</span>

    </div>

    <div class="block">

    List of chains to be excluded. A place can be assigned multiple chains. If any of them is in CategoryQuery.excludeChains , that place will not be included in the response, regardless of whether any of its assigned chains have been included in CategoryQuery.includeChains . In short, an exclusion will always win over an inclusion.

    </div>

    </div>

  - <div id="sdk-for-android-explore-includeFoodTypes" class="section detail">

    ### includeFoodTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>\></span> <span class="element-name">includeFoodTypes</span>

    </div>

    <div class="block">

    List of food types to be included. A place can be assigned multiple food types. If any of them is in CategoryQuery.includeFoodTypes , but none are in CategoryQuery.excludeFoodTypes , that place will be included in the response.

    </div>

    </div>

  - <div id="sdk-for-android-explore-excludeFoodTypes" class="section detail">

    ### excludeFoodTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placefoodtype" title="class in com.here.sdk.search">PlaceFoodType</a>\></span> <span class="element-name">excludeFoodTypes</span>

    </div>

    <div class="block">

    List of food types to be excluded. A place can be assigned multiple food types. If any of them is in CategoryQuery.excludeFoodTypes , that place will not be included in the response, regardless of whether any of its assigned food types have been included in CategoryQuery.includeFoodTypes . In short, an exclusion will always win over an inclusion.

    </div>

    </div>

  - <div id="sdk-for-android-explore-filter" class="section detail">

    ### filter

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">filter</span>

    </div>

    <div class="block">

    Full-text filter on POI names/titles. Results with a partial match are included in the response. By default the value is set to null and results will be based on other parameters provided.

    </div>

    </div>

  - <div id="sdk-for-android-explore-placeFilter" class="section detail">

    ### placeFilter

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-search-placefilter" title="class in com.here.sdk.search">PlaceFilter</a></span> <span class="element-name">placeFilter</span>

    </div>

    <div class="block">

    The filter options to specify a place in query. Consists of fuel and truck options.

    </div>

    </div>

  - <div id="sdk-for-android-explore-area" class="section detail">

    ### area

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a></span> <span class="element-name">area</span>

    </div>

    <div class="block">

    Area in which to provide the most relevant places.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-search-PlaceCategory-com-here-sdk-search-CategoryQuery-Area" class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a> category, @NonNull <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `category` -

    Category for query

    `area` -

    Area in which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-explore-init-java-util-List-com-here-sdk-search-CategoryQuery-Area" class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>\> categories, @NonNull <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `categories` -

    List of categories.

    `area` -

    Area in which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-search-PlaceCategory-java-lang-String-com-here-sdk-search-CategoryQuery-Area" class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a> category, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> filter, @NonNull <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `category` -

    Category for query

    `filter` -

    Full-text filter on POI names/titles. Results with a partial match are included in the response.

    `area` -

    Area in which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-explore-init-java-util-List-java-lang-String-com-here-sdk-search-CategoryQuery-Area" class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-search-placecategory" title="class in com.here.sdk.search">PlaceCategory</a>\> categories, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> filter, @NonNull <a href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area" title="class in com.here.sdk.search">CategoryQuery.Area</a> area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `categories` -

    List of categories.

    `filter` -

    Full-text filter on POI names/titles. Results with a partial match are included in the response.

    `area` -

    Area in which to provide the most relevant places.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

