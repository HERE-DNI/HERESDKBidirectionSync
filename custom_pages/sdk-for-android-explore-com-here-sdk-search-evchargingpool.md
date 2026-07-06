---
title: "EVChargingPool (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evchargingpool"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.EVChargingPool

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVChargingPool</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A charging pool for electric vehicles is an area equipped with one or
more charging stations. Use
PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION to find
stations. In the Details of a Place result you can find the list of
found pools containing stations, if any. For offline EV rich attributes,
also enable LayerConfiguration.Feature.EV in
SDKOptions.layerConfiguration .

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  [`EVAccessType`](sdk-for-android-explore-com-here-sdk-search-evaccesstype "enum class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#access"
  class="member-name-link"><code>access</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The accessibility level of the charging pool, or null if unknown.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`EVAccessRestrictionReason`](sdk-for-android-explore-com-here-sdk-search-evaccessrestrictionreason "enum class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#accessRestrictionReasons"
  class="member-name-link"><code>accessRestrictionReasons</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Contains the list of reasons for restriction.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`EVChargingStation`](sdk-for-android-explore-com-here-sdk-search-evchargingstation "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#chargingStations"
  class="member-name-link"><code>chargingStations</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of charging stations.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#cpoId"
  class="member-name-link"><code>cpoId</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  CPO (Charge Point Operator) id for charging pool.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`EVChargingPoolDetails`](sdk-for-android-explore-com-here-sdk-search-evchargingpooldetails "class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#details"
  class="member-name-link"><code>details</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EV charging station attributes details.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`EMobilityServiceProvider`](sdk-for-android-explore-com-here-sdk-search-emobilityserviceprovider "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#eMobilityServiceProviders"
  class="member-name-link"><code>eMobilityServiceProviders</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of e-Mobility Service Providers.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`Evse`](sdk-for-android-explore-com-here-sdk-search-evse "class in com.here.sdk.search")`>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#evseInfo"
  class="member-name-link"><code>evseInfo</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Charge Point Operator (CPO) ID uses the Electric Vehicle Supply
  Equipment ID (EVSE ID) for an exact identification of the charging
  infrastructure and charging point.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingpool#id"
  class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  HERE ID of the charging pool.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      EVChargingPool(List<EVChargingStation> chargingStations,
       List<EMobilityServiceProvider> eMobilityServiceProviders,
       List<EVAccessRestrictionReason> accessRestrictionReasons)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-chargingStations"
    class="section detail">

    ### chargingStations

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVChargingStation](sdk-for-android-explore-com-here-sdk-search-evchargingstation "class in com.here.sdk.search")\></span> <span class="element-name">chargingStations</span>

    </div>

    <div class="block">

    List of charging stations.

    </div>

    </div>

  - <div id="sdk-for-android-explore-eMobilityServiceProviders"
    class="section detail">

    ### eMobilityServiceProviders

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EMobilityServiceProvider](sdk-for-android-explore-com-here-sdk-search-emobilityserviceprovider "class in com.here.sdk.search")\></span> <span class="element-name">eMobilityServiceProviders</span>

    </div>

    <div class="block">

    List of e-Mobility Service Providers. Only online search fills this
    field.

    </div>

    </div>

  - <div id="sdk-for-android-explore-access" class="section detail">

    ### access

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVAccessType](sdk-for-android-explore-com-here-sdk-search-evaccesstype "enum class in com.here.sdk.search")</span> <span class="element-name">access</span>

    </div>

    <div class="block">

    The accessibility level of the charging pool, or null if unknown.

    </div>

    </div>

  - <div id="sdk-for-android-explore-accessRestrictionReasons"
    class="section detail">

    ### accessRestrictionReasons

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVAccessRestrictionReason](sdk-for-android-explore-com-here-sdk-search-evaccessrestrictionreason "enum class in com.here.sdk.search")\></span> <span class="element-name">accessRestrictionReasons</span>

    </div>

    <div class="block">

    Contains the list of reasons for restriction. Populated only for
    offline search and when access is EVAccessType.RESTRICTED_ACCESS .

    </div>

    </div>

  - <div id="sdk-for-android-explore-details" class="section detail">

    ### details

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingPoolDetails](sdk-for-android-explore-com-here-sdk-search-evchargingpooldetails "class in com.here.sdk.search")</span> <span class="element-name">details</span>

    </div>

    <div class="block">

    EV charging station attributes details. It is available only for a
    place that has charging station for electric vehicles. Only offline
    search fills this field. Note: Not available as part of Suggestion
    results.

    </div>

    </div>

  - <div id="sdk-for-android-explore-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span>

    </div>

    <div class="block">

    HERE ID of the charging pool. Only online search fills this field.

    </div>

    </div>

  - <div id="sdk-for-android-explore-cpoId" class="section detail">

    ### cpoId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">cpoId</span>

    </div>

    <div class="block">

    CPO (Charge Point Operator) id for charging pool. Only online search
    fills this field.

    </div>

    </div>

  - <div id="sdk-for-android-explore-evseInfo" class="section detail">

    ### evseInfo

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Evse](sdk-for-android-explore-com-here-sdk-search-evse "class in com.here.sdk.search")\></span> <span class="element-name">evseInfo</span>

    </div>

    <div class="block">

    Charge Point Operator (CPO) ID uses the Electric Vehicle Supply
    Equipment ID (EVSE ID) for an exact identification of the charging
    infrastructure and charging point. Only online search fills this
    field.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List,java.util.List)"
    class="section detail">

    ### EVChargingPool

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVChargingPool</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVChargingStation](sdk-for-android-explore-com-here-sdk-search-evchargingstation "class in com.here.sdk.search")\> chargingStations,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EMobilityServiceProvider](sdk-for-android-explore-com-here-sdk-search-emobilityserviceprovider "class in com.here.sdk.search")\> eMobilityServiceProviders,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[EVAccessRestrictionReason](sdk-for-android-explore-com-here-sdk-search-evaccessrestrictionreason "enum class in com.here.sdk.search")\> accessRestrictionReasons)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `chargingStations` -

    List of charging stations.

    `eMobilityServiceProviders` -

    List of e-Mobility Service Providers. Only online search fills this
    field.

    `accessRestrictionReasons` -

    Contains the list of reasons for restriction. Populated only for
    offline search and when access is
    [`EVAccessType.RESTRICTED_ACCESS`](sdk-for-android-explore-com-here-sdk-search-evaccesstype#RESTRICTED_ACCESS).

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

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

