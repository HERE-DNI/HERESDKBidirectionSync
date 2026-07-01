---
title: "GeoPlace (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-geoplace"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.GeoPlace

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoPlace</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

GeoPlace struct represents a location object: such as a country, a city,
a point of interest (POI) etc. It can be used for PersonalPlace
creation, in order to provide search on custom places.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address"
  title="class in com.here.sdk.search"><code>Address</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-geoplace#address"
  class="member-name-link"><code>address</code></a></td>
  <td><div class="block">
  Address of the place Note: Address can have default value when no data
  is available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-businessdetails"
  title="class in com.here.sdk.search"><code>BusinessDetails</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-geoplace#business"
  class="member-name-link"><code>business</code></a></td>
  <td><div class="block">
  Business details Note: BusinessDetails can have default value when no
  data is available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placecategory"
  title="class in com.here.sdk.search"><code>PlaceCategory</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-geoplace#categories"
  class="member-name-link"><code>categories</code></a></td>
  <td><div class="block">
  List of corresponding categories Note: This list can be empty when no
  data is available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-externalid"
  title="class in com.here.sdk.core"><code>ExternalID</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-geoplace#externalIDs"
  class="member-name-link"><code>externalIDs</code></a></td>
  <td><div class="block">
  Allows the client to set the id in their own system.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-locationdetails"
  title="class in com.here.sdk.search"><code>LocationDetails</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-geoplace#location"
  class="member-name-link"><code>location</code></a></td>
  <td><div class="block">
  Geographical details Note: Can be null when retrieved from a
  suggestion's place property.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-geoplace#title"
  class="member-name-link"><code>title</code></a></td>
  <td><div class="block">
  The localized title for the resource.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-placetype"
  title="enum class in com.here.sdk.search"><code>PlaceType</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-geoplace#type"
  class="member-name-link"><code>type</code></a></td>
  <td><div class="block">
  Specifies place type.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-webdetails"
  title="class in com.here.sdk.search"><code>WebDetails</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-geoplace#web"
  class="member-name-link"><code>web</code></a></td>
  <td><div class="block">
  Contains info and direct web links to corresponding items.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>GeoPlace()</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getID()</code></pre></td>
  <td><div class="block">
  Allow the client to access GeoPlace id.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isMyPlace()</code></pre></td>
  <td><div class="block">
  Allow the client to access info about is it my place or not.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-search-geoplace"
  title="class in com.here.sdk.search"><code>GeoPlace</code></a></td>
  <td><pre><code>makeMyPlace(String title,
   GeoCoordinates coordinates)</code></pre></td>
  <td><div class="block">
  Creates a new instance of this class.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="title" class="section detail">

    ### title

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">title</span>

    </div>

    <div class="block">

    The localized title for the resource. Note: This String can be empty
    when no data is available.

    </div>

    </div>

  - <div id="externalIDs" class="section detail">

    ### externalIDs

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[ExternalID](sdk-for-android-explore-com-here-sdk-core-externalid "class in com.here.sdk.core")></span> <span class="element-name">externalIDs</span>

    </div>

    <div class="block">

    Allows the client to set the id in their own system. The list of
    supplier references to this place. The references are provided by
    external suppliers and are only available to users with valid
    contracts with said suppliers. If the user has no such contracts,
    the list is empty.

    </div>

    </div>

  - <div id="type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PlaceType](sdk-for-android-explore-com-here-sdk-search-placetype "enum class in com.here.sdk.search")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    Specifies place type.

    </div>

    </div>

  - <div id="categories" class="section detail">

    ### categories

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")></span> <span class="element-name">categories</span>

    </div>

    <div class="block">

    List of corresponding categories Note: This list can be empty when
    no data is available.

    </div>

    </div>

  - <div id="address" class="section detail">

    ### address

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Address](sdk-for-android-explore-com-here-sdk-search-address "class in com.here.sdk.search")</span> <span class="element-name">address</span>

    </div>

    <div class="block">

    Address of the place Note: Address can have default value when no
    data is available.

    </div>

    </div>

  - <div id="location" class="section detail">

    ### location

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[LocationDetails](sdk-for-android-explore-com-here-sdk-search-locationdetails "class in com.here.sdk.search")</span> <span class="element-name">location</span>

    </div>

    <div class="block">

    Geographical details Note: Can be null when retrieved from a
    suggestion's place property.

    </div>

    </div>

  - <div id="business" class="section detail">

    ### business

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[BusinessDetails](sdk-for-android-explore-com-here-sdk-search-businessdetails "class in com.here.sdk.search")</span> <span class="element-name">business</span>

    </div>

    <div class="block">

    Business details Note: BusinessDetails can have default value when
    no data is available.

    </div>

    </div>

  - <div id="web" class="section detail">

    ### web

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[WebDetails](sdk-for-android-explore-com-here-sdk-search-webdetails "class in com.here.sdk.search")</span> <span class="element-name">web</span>

    </div>

    <div class="block">

    Contains info and direct web links to corresponding items. Note:
    WebDetails can have default value when no data is available.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### GeoPlace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPlace</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="makeMyPlace(java.lang.String,com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### makeMyPlace

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[GeoPlace](sdk-for-android-explore-com-here-sdk-search-geoplace "class in com.here.sdk.search")</span> <span class="element-name">makeMyPlace</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> title,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Creates a new instance of this class. All other properties will keep
    their default value and all properties containing lists will contain
    empty lists.

    </div>

    Parameters:  
    `title` -

    The title.

    `coordinates` -

    The coordinates.

    Returns:  
    An instance of
    [`GeoPlace`](sdk-for-android-explore-com-here-sdk-search-geoplace "class in com.here.sdk.search").

    </div>

  - <div id="getID()" class="section detail">

    ### getID

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()

    </div>

    <div class="block">

    Allow the client to access GeoPlace id.

    </div>

    Returns:  
    The place id.

    </div>

  - <div id="isMyPlace()" class="section detail">

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

</div>

