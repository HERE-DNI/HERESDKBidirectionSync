---
title: "AvoidanceOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.AvoidanceOptions → com.here.sdk.routing.AvoidanceOptions

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AvoidanceOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify restrictions for route calculations.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`AvoidBoundingBoxAreaOptions`](sdk-for-android-explore-com-here-sdk-routing-avoidboundingboxareaoptions "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#avoidBoundingBoxAreasOptions" class="member-name-link"><code>avoidBoundingBoxAreasOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of rectangular shapes which routes must not cross and additional options for this area.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`AvoidCorridorAreaOptions`](sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#avoidCorridorAreasOptions" class="member-name-link"><code>avoidCorridorAreasOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of corridor shapes which routes must not cross and additional options for this area.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`TruckRoadType`](sdk-for-android-explore-com-here-sdk-transport-truckroadtype "enum class in com.here.sdk.transport")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#avoidedTruckRoadTypes" class="member-name-link"><code>avoidedTruckRoadTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies a list of avoided truck road types for vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`AvoidPolygonAreaOptions`](sdk-for-android-explore-com-here-sdk-routing-avoidpolygonareaoptions "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#avoidPolygonAreasOptions" class="member-name-link"><code>avoidPolygonAreasOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of polygon shapes which routes must not cross and additional options for this area.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`CountryCode`](sdk-for-android-explore-com-here-sdk-core-countrycode "enum class in com.here.sdk.core")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#countries" class="member-name-link"><code>countries</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Countries that the route must avoid.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#exceptZoneIds" class="member-name-link"><code>exceptZoneIds</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Exception to AvoidanceOptions.zone_categories , which can be specified by list of zone identifiers.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`RoadFeatures`](sdk-for-android-explore-com-here-sdk-routing-roadfeatures "enum class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#roadFeatures" class="member-name-link"><code>roadFeatures</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Features which routes should avoid.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`SegmentReference`](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#segments" class="member-name-link"><code>segments</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Segments that routes will avoid going through.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`ZoneCategory`](sdk-for-android-explore-com-here-sdk-routing-zonecategory "enum class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#zoneCategories" class="member-name-link"><code>zoneCategories</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Zone categories which routes must not cross.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions#zoneIds" class="member-name-link"><code>zoneIds</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List containing identifiers of zones that routes should avoid going through.

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

      AvoidanceOptions ()

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

  - <div id="sdk-for-android-explore-roadFeatures" class="section detail">

    ### roadFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RoadFeatures](sdk-for-android-explore-com-here-sdk-routing-roadfeatures "enum class in com.here.sdk.routing")\></span> <span class="element-name">roadFeatures</span>

    </div>

    <div class="block">

    Features which routes should avoid. Best effort only (not enforced).

    </div>

    </div>

  - <div id="sdk-for-android-explore-countries" class="section detail">

    ### countries

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[CountryCode](sdk-for-android-explore-com-here-sdk-core-countrycode "enum class in com.here.sdk.core")\></span> <span class="element-name">countries</span>

    </div>

    <div class="block">

    Countries that the route must avoid. Strictly enforced. Violations are reported as SectionNoticeCode.VIOLATED_BLOCKED_ROAD . Note: This avoidance option is not supported in IsolineOptions for isoline calculation.

    </div>

    </div>

  - <div id="sdk-for-android-explore-avoidBoundingBoxAreasOptions" class="section detail">

    ### avoidBoundingBoxAreasOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[AvoidBoundingBoxAreaOptions](sdk-for-android-explore-com-here-sdk-routing-avoidboundingboxareaoptions "class in com.here.sdk.routing")\></span> <span class="element-name">avoidBoundingBoxAreasOptions</span>

    </div>

    <div class="block">

    List of rectangular shapes which routes must not cross and additional options for this area.

    </div>

    </div>

  - <div id="sdk-for-android-explore-avoidPolygonAreasOptions" class="section detail">

    ### avoidPolygonAreasOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[AvoidPolygonAreaOptions](sdk-for-android-explore-com-here-sdk-routing-avoidpolygonareaoptions "class in com.here.sdk.routing")\></span> <span class="element-name">avoidPolygonAreasOptions</span>

    </div>

    <div class="block">

    List of polygon shapes which routes must not cross and additional options for this area. Note: Currently, the maximum count of polygons is limited to 20.

    </div>

    </div>

  - <div id="sdk-for-android-explore-avoidCorridorAreasOptions" class="section detail">

    ### avoidCorridorAreasOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[AvoidCorridorAreaOptions](sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions "class in com.here.sdk.routing")\></span> <span class="element-name">avoidCorridorAreasOptions</span>

    </div>

    <div class="block">

    List of corridor shapes which routes must not cross and additional options for this area. Note: Currently, the maximum count of corridors is limited to 20.

    </div>

    </div>

  - <div id="sdk-for-android-explore-zoneCategories" class="section detail">

    ### zoneCategories

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[ZoneCategory](sdk-for-android-explore-com-here-sdk-routing-zonecategory "enum class in com.here.sdk.routing")\></span> <span class="element-name">zoneCategories</span>

    </div>

    <div class="block">

    Zone categories which routes must not cross. Strictly enforced. Violations are reported as SectionNoticeCode.VIOLATED_ZONE_RESTRICTION .

    </div>

    </div>

  - <div id="sdk-for-android-explore-segments" class="section detail">

    ### segments

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[SegmentReference](sdk-for-android-explore-com-here-sdk-routing-segmentreference "class in com.here.sdk.routing")\></span> <span class="element-name">segments</span>

    </div>

    <div class="block">

    Segments that routes will avoid going through. Violations are reported as SectionNoticeCode.VIOLATED_BLOCKED_ROAD . Notes: This avoidance option is not supported in IsolineOptions for isoline calculation. The engine does not support an unlimited number of segments to avoid. The limit is defined by the HERE backend services and may change. For now, the maximum number of segments to avoid should be below 250. This value may change on the backend and it is therefore not guaranteed to be stable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-exceptZoneIds" class="section detail">

    ### exceptZoneIds

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\></span> <span class="element-name">exceptZoneIds</span>

    </div>

    <div class="block">

    Exception to AvoidanceOptions.zone_categories , which can be specified by list of zone identifiers. e.g. the format of ID is like here:cm:envzone:2 . Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".

    </div>

    </div>

  - <div id="sdk-for-android-explore-zoneIds" class="section detail">

    ### zoneIds

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\></span> <span class="element-name">zoneIds</span>

    </div>

    <div class="block">

    List containing identifiers of zones that routes should avoid going through. e.g. the format of ID is like here:cm:envzone:2 . Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".

    </div>

    </div>

  - <div id="sdk-for-android-explore-avoidedTruckRoadTypes" class="section detail">

    ### avoidedTruckRoadTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[TruckRoadType](sdk-for-android-explore-com-here-sdk-transport-truckroadtype "enum class in com.here.sdk.transport")\></span> <span class="element-name">avoidedTruckRoadTypes</span>

    </div>

    <div class="block">

    Specifies a list of avoided truck road types for vehicle. Refer to TruckRoadType for the available options.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### AvoidanceOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AvoidanceOptions</span>()

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

  </div>

<!-- ========= END OF CLASS DATA ========= -->

