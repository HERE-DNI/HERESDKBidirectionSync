---
title: "PhysicalAttributes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.PhysicalAttributes → com.here.sdk.mapdata.PhysicalAttributes

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">PhysicalAttributes</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Physical attributes of the segment. Note a road can have more than one attribute at the same time. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

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

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-roaddivider" title="enum class in com.here.sdk.mapdata">`RoadDivider`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#divider" class="member-name-link"><code>divider</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates the presence of a road divider.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isBoatFerry" class="member-name-link"><code>isBoatFerry</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Identifies a generalised route of a boat ferry for passengers or vehicles over water.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isBridge" class="member-name-link"><code>isBridge</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Identifies a structure that allows a road, railway, or walkway to pass over another road, railway, waterway, or valley serving map display and route guidance functionalities.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isDirtRoad" class="member-name-link"><code>isDirtRoad</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates whether the navigable segment is paved.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isMultiplyDigitized" class="member-name-link"><code>isMultiplyDigitized</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Identifies separately digitised roads, i.e., roads that are digitised with one line per direction of traffic instead of one line per road.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isPrivate" class="member-name-link"><code>isPrivate</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Private identifies roads that are not maintained by an organization responsible for maintenance of public roads.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isRailFerry" class="member-name-link"><code>isRailFerry</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Identifies a generalised route of a ferry for passengers or vehicles via rail.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isRoundabout" class="member-name-link"><code>isRoundabout</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates the presence of a roundabout.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isTunnel" class="member-name-link"><code>isTunnel</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Identifies an enclosed (on all sides) passageway through or under an obstruction.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      PhysicalAttributes ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance with default values.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-isDirtRoad" class="section detail">

    ### isDirtRoad

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirtRoad</span>

    </div>

    <div class="block">

    Indicates whether the navigable segment is paved. Paved is primarily used for map display and routing by assigning higher penalties to unpaved roads. Paved roads are made of concrete, asphalt, cobblestone or brick. Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isTunnel" class="section detail">

    ### isTunnel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTunnel</span>

    </div>

    <div class="block">

    Identifies an enclosed (on all sides) passageway through or under an obstruction. This attribute can be used for display or route guidance.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isBridge" class="section detail">

    ### isBridge

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBridge</span>

    </div>

    <div class="block">

    Identifies a structure that allows a road, railway, or walkway to pass over another road, railway, waterway, or valley serving map display and route guidance functionalities. Bridge is published on segments that represent significant bridges and/or overpasses; elevated roads are not published as bridge.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isPrivate" class="section detail">

    ### isPrivate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrivate</span>

    </div>

    <div class="block">

    Private identifies roads that are not maintained by an organization responsible for maintenance of public roads. Allows for unique cartographic representation of roads that restrict public use. May be used to avoid routing through a private road.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isRoundabout" class="section detail">

    ### isRoundabout

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRoundabout</span>

    </div>

    <div class="block">

    Indicates the presence of a roundabout.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isMultiplyDigitized" class="section detail">

    ### isMultiplyDigitized

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMultiplyDigitized</span>

    </div>

    <div class="block">

    Identifies separately digitised roads, i.e., roads that are digitised with one line per direction of traffic instead of one line per road. It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus lane) are located between the separately digitised opposing roadbeds if driver perception remains unchanged.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-divider" class="section detail">

    ### divider

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-roaddivider" title="enum class in com.here.sdk.mapdata">RoadDivider</a></span> <span class="element-name">divider</span>

    </div>

    <div class="block">

    Indicates the presence of a road divider.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isBoatFerry" class="section detail">

    ### isBoatFerry

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBoatFerry</span>

    </div>

    <div class="block">

    Identifies a generalised route of a boat ferry for passengers or vehicles over water.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isRailFerry" class="section detail">

    ### isRailFerry

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRailFerry</span>

    </div>

    <div class="block">

    Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied on a segment that represent a ferry route for vehicles over rail such as: a route for ferrying passengers over rail, if destination is not accessible by the road network or prohibits the use of automobiles.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### PhysicalAttributes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PhysicalAttributes</span>()

    </div>

    <div class="block">

    Creates a new instance with default values.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

