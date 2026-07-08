---
title: "EVChargingLocationFeature (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< EVChargingLocationFeature \> com.here.sdk.search.EVChargingLocationFeature → java.lang.Enum \< EVChargingLocationFeature \> com.here.sdk.search.EVChargingLocationFeature → com.here.sdk.search.EVChargingLocationFeature

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`[`EVChargingLocationFeature`](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">EVChargingLocationFeature</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")\></span>

</div>

<div class="block">

Optional features that can be requested for EV charging locations. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#CONNECTOR_GROUPS" class="member-name-link"><code>CONNECTOR_GROUPS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVChargingLocation.getConnectorGroups() will be returned.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#EMSPS" class="member-name-link"><code>EMSPS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVChargingLocation.getEMobilityServiceProviders() will be returned.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#EVSES" class="member-name-link"><code>EVSES</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVChargingLocation.getEvses() will be returned.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#LOCATION_INFO" class="member-name-link"><code>LOCATION_INFO</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVChargingLocation.getCpoID() , EVChargingLocation.getFacilityTypes() , EVChargingLocation.getParkingType() , EVChargingLocation.getEnergyMix() , and EVChargingLocation.getOpeningHours() will be returned.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#NEARBY" class="member-name-link"><code>NEARBY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVChargingLocation.getFacilityTypes() will be returned.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#TARIFFS" class="member-name-link"><code>TARIFFS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVChargingConnectorGroup.tariffIndexes will be returned.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature#TRUCK_RESTRICTIONS" class="member-name-link"><code>TRUCK_RESTRICTIONS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVChargingLocation.getTruckRestrictions() will be returned.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`EVChargingLocationFeature`](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`EVChargingLocationFeature`](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-EVSES" class="section detail">

    ### EVSES

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">EVSES</span>

    </div>

    <div class="block">

    EVChargingLocation.getEvses() will be returned. If CONNECTOR_GROUPS is also included, then EVChargingConnectorGroup.connectors will also be returned.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRUCK_RESTRICTIONS" class="section detail">

    ### TRUCK_RESTRICTIONS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">TRUCK_RESTRICTIONS</span>

    </div>

    <div class="block">

    EVChargingLocation.getTruckRestrictions() will be returned.

    </div>

    </div>

  - <div id="sdk-for-android-explore-LOCATION_INFO" class="section detail">

    ### LOCATION_INFO

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">LOCATION_INFO</span>

    </div>

    <div class="block">

    EVChargingLocation.getCpoID() , EVChargingLocation.getFacilityTypes() , EVChargingLocation.getParkingType() , EVChargingLocation.getEnergyMix() , and EVChargingLocation.getOpeningHours() will be returned.

    </div>

    </div>

  - <div id="sdk-for-android-explore-EMSPS" class="section detail">

    ### EMSPS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">EMSPS</span>

    </div>

    <div class="block">

    EVChargingLocation.getEMobilityServiceProviders() will be returned.

    </div>

    </div>

  - <div id="sdk-for-android-explore-CONNECTOR_GROUPS" class="section detail">

    ### CONNECTOR_GROUPS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">CONNECTOR_GROUPS</span>

    </div>

    <div class="block">

    EVChargingLocation.getConnectorGroups() will be returned. To ensure EVChargingConnectorGroup.connectors is available, also include EVSES . To ensure EVChargingConnectorGroup.tariffIndexes is available, also include TARIFFS .

    </div>

    </div>

  - <div id="sdk-for-android-explore-TARIFFS" class="section detail">

    ### TARIFFS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">TARIFFS</span>

    </div>

    <div class="block">

    EVChargingConnectorGroup.tariffIndexes will be returned. Ignored if neither EVSES nor CONNECTOR_GROUPS are included.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NEARBY" class="section detail">

    ### NEARBY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">NEARBY</span>

    </div>

    <div class="block">

    EVChargingLocation.getFacilityTypes() will be returned.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[EVChargingLocationFeature](sdk-for-android-explore-com-here-sdk-search-evcharginglocationfeature "enum class in com.here.sdk.search")</span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

