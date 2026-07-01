---
title: "PlaceFilter (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-placefilter"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.PlaceFilter

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PlaceFilter</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The filter options to specify a place. Consists of fuel, truck and EV
options.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

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
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static final class </code></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-placefilter-ev"
  class="type-name-link"
  title="class in com.here.sdk.search"><code>PlaceFilter.Ev</code></a></td>
  <td><div class="block">
  Constraints that are applicable on the places of category EV station.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><a href="sdk-for-android-explore-com-here-sdk-search-placefilter-ev"
  title="class in com.here.sdk.search"><code>PlaceFilter.Ev</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-placefilter#ev"
  class="member-name-link"><code>ev</code></a></td>
  <td><div class="block">
  Constraints that are applicable on the places of category EV station.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-transport-fueltype"
  title="enum class in com.here.sdk.transport"><code>FuelType</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-placefilter#fuelTypes"
  class="member-name-link"><code>fuelTypes</code></a></td>
  <td><div class="block">
  The list of FuelType elements that should be used to find only the
  FuelStation search results that support all of them.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-transport-truckclass"
  title="enum class in com.here.sdk.transport"><code>TruckClass</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-placefilter#truckClass"
  class="member-name-link"><code>truckClass</code></a></td>
  <td><div class="block">
  Should be used to find only the FuelStation search results with minimum
  supported TruckClass .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-transport-truckfueltype"
  title="enum class in com.here.sdk.transport"><code>TruckFuelType</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-placefilter#truckFuelTypes"
  class="member-name-link"><code>truckFuelTypes</code></a></td>
  <td><div class="block">
  The list of TruckFuelType elements that should be used to find only the
  FuelStation search results that support all of them.
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
  <td><pre><code>PlaceFilter()</code></pre></td>
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
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
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

  - <div id="fuelTypes" class="section detail">

    ### fuelTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[FuelType](sdk-for-android-explore-com-here-sdk-transport-fueltype "enum class in com.here.sdk.transport")></span> <span class="element-name">fuelTypes</span>

    </div>

    <div class="block">

    The list of FuelType elements that should be used to find only the
    FuelStation search results that support all of them. This filter is
    available to use with the SearchEngine and OfflineSearchEngine (only
    available for the Navigate license), however OfflineSearchEngine
    supports it only for searchByText and searchByCategory with allowed
    fuel types DIESEL , LPG , BIO_DIESEL , CNG , DIESEL_WITH_ADDITIVES ,
    E10 , E85 , ETHANOL , ETHANOL_WITH_ADDITIVES , GASOLINE , HYDROGEN ,
    LNG , MIDGRADE , PREMIUM and REGULAR . Note: This is a beta release
    of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    </div>

  - <div id="truckFuelTypes" class="section detail">

    ### truckFuelTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[TruckFuelType](sdk-for-android-explore-com-here-sdk-transport-truckfueltype "enum class in com.here.sdk.transport")></span> <span class="element-name">truckFuelTypes</span>

    </div>

    <div class="block">

    The list of TruckFuelType elements that should be used to find only
    the FuelStation search results that support all of them. Not
    supported for suggestByText in OfflineSearchEngine (only available
    for the Navigate license). Note: This is a beta release of this
    feature, so there could be a few bugs and unexpected behaviors.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    </div>

  - <div id="truckClass" class="section detail">

    ### truckClass

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TruckClass](sdk-for-android-explore-com-here-sdk-transport-truckclass "enum class in com.here.sdk.transport")</span> <span class="element-name">truckClass</span>

    </div>

    <div class="block">

    Should be used to find only the FuelStation search results with
    minimum supported TruckClass . This filter is only available to use
    with the SearchEngine . The OfflineSearchEngine (only available for
    the Navigate license) does not apply this filter.
    TruckClass.LIGHT_CLASS is not accepted in the filter. Otherwise will
    result in SearchError.INVALID_TRUCK_CLASS . Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    </div>

  - <div id="ev" class="section detail">

    ### ev

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PlaceFilter.Ev](sdk-for-android-explore-com-here-sdk-search-placefilter-ev "class in com.here.sdk.search")</span> <span class="element-name">ev</span>

    </div>

    <div class="block">

    Constraints that are applicable on the places of category EV
    station.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### PlaceFilter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PlaceFilter</span>()

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

  </div>

</div>

