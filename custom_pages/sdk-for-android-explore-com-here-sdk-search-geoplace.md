---
title: "GeoPlace (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-geoplace"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.search.GeoPlace → com.here.sdk.search.GeoPlace

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">GeoPlace</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

GeoPlace struct represents a location object: such as a country, a city, a point of interest (POI) etc. It can be used for PersonalPlace creation, in order to provide search on custom places.

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

  [`Address`](sdk-for-android-explore-com-here-sdk-search-address "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#address" class="member-name-link"><code>address</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Address of the place Note: Address can have default value when no data is available.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`BusinessDetails`](sdk-for-android-explore-com-here-sdk-search-businessdetails "class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#business" class="member-name-link"><code>business</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Business details Note: BusinessDetails can have default value when no data is available.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`PlaceCategory`](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#categories" class="member-name-link"><code>categories</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of corresponding categories Note: This list can be empty when no data is available.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`ExternalID`](sdk-for-android-explore-com-here-sdk-core-externalid "class in com.here.sdk.core")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#externalIDs" class="member-name-link"><code>externalIDs</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Allows the client to set the id in their own system.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`LocationDetails`](sdk-for-android-explore-com-here-sdk-search-locationdetails "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#location" class="member-name-link"><code>location</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Geographical details Note: Can be null when retrieved from a suggestion's place property.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#title" class="member-name-link"><code>title</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The localized title for the resource.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`PlaceType`](sdk-for-android-explore-com-here-sdk-search-placetype "enum class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#type" class="member-name-link"><code>type</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies place type.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`WebDetails`](sdk-for-android-explore-com-here-sdk-search-webdetails "class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-geoplace#web" class="member-name-link"><code>web</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Contains info and direct web links to corresponding items.

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

      GeoPlace ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getID ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Allow the client to access GeoPlace id.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isMyPlace ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Allow the client to access info about is it my place or not.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`GeoPlace`](sdk-for-android-explore-com-here-sdk-search-geoplace "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      makeMyPlace ( String title, GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a new instance of this class.

  </div>

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

  - <div id="sdk-for-android-explore-title" class="section detail">

    ### title

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">title</span>

    </div>

    <div class="block">

    The localized title for the resource. Note: This String can be empty when no data is available.

    </div>

    </div>

  - <div id="sdk-for-android-explore-externalIDs" class="section detail">

    ### externalIDs

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[ExternalID](sdk-for-android-explore-com-here-sdk-core-externalid "class in com.here.sdk.core")\></span> <span class="element-name">externalIDs</span>

    </div>

    <div class="block">

    Allows the client to set the id in their own system. The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

    </div>

    </div>

  - <div id="sdk-for-android-explore-type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[PlaceType](sdk-for-android-explore-com-here-sdk-search-placetype "enum class in com.here.sdk.search")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Specifies place type.

    </div>

    </div>

  - <div id="sdk-for-android-explore-categories" class="section detail">

    ### categories

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")\></span> <span class="element-name">categories</span>

    </div>

    <div class="block">

    List of corresponding categories Note: This list can be empty when no data is available.

    </div>

    </div>

  - <div id="sdk-for-android-explore-address" class="section detail">

    ### address

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Address](sdk-for-android-explore-com-here-sdk-search-address "class in com.here.sdk.search")</span> <span class="element-name">address</span>

    </div>

    <div class="block">

    Address of the place Note: Address can have default value when no data is available.

    </div>

    </div>

  - <div id="sdk-for-android-explore-location" class="section detail">

    ### location

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[LocationDetails](sdk-for-android-explore-com-here-sdk-search-locationdetails "class in com.here.sdk.search")</span> <span class="element-name">location</span>

    </div>

    <div class="block">

    Geographical details Note: Can be null when retrieved from a suggestion's place property.

    </div>

    </div>

  - <div id="sdk-for-android-explore-business" class="section detail">

    ### business

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[BusinessDetails](sdk-for-android-explore-com-here-sdk-search-businessdetails "class in com.here.sdk.search")</span> <span class="element-name">business</span>

    </div>

    <div class="block">

    Business details Note: BusinessDetails can have default value when no data is available.

    </div>

    </div>

  - <div id="sdk-for-android-explore-web" class="section detail">

    ### web

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[WebDetails](sdk-for-android-explore-com-here-sdk-search-webdetails "class in com.here.sdk.search")</span> <span class="element-name">web</span>

    </div>

    <div class="block">

    Contains info and direct web links to corresponding items. Note: WebDetails can have default value when no data is available.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### GeoPlace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPlace</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

  - <div id="sdk-for-android-explore-makeMyPlace-java-lang-String-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### makeMyPlace

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type">[GeoPlace](sdk-for-android-explore-com-here-sdk-search-geoplace "class in com.here.sdk.search")</span> <span class="element-name">makeMyPlace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> title, @NonNull [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Creates a new instance of this class. All other properties will keep their default value and all properties containing lists will contain empty lists.

    </div>

    Parameters:  
    `title` -

    The title.

    `coordinates` -

    The coordinates.

    Returns:  
    An instance of [`GeoPlace`](sdk-for-android-explore-com-here-sdk-search-geoplace "class in com.here.sdk.search").

    </div>

  - <div id="sdk-for-android-explore-getID" class="section detail">

    ### getID

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()

    </div>

    <div class="block">

    Allow the client to access GeoPlace id.

    </div>

    Returns:  
    The place id.

    </div>

  - <div id="sdk-for-android-explore-isMyPlace" class="section detail">

    ### isMyPlace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMyPlace</span>()

    </div>

    <div class="block">

    Allow the client to access info about is it my place or not.

    </div>

    Returns:  
    `True` if it is my place, `false` otherwise.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

