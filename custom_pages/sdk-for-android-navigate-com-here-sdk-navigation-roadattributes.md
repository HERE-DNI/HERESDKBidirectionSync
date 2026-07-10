---
title: "RoadAttributes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadattributes"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.RoadAttributes → com.here.sdk.navigation.RoadAttributes

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RoadAttributes</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Road attributes, including usage and physical characteristics. Note that a road can have more than one attribute at the same time.

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

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isBridge" class="member-name-link"><code>isBridge</code></a>

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isBuiltUpArea" class="member-name-link"><code>isBuiltUpArea</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Indicates if the navigable segment is a built up area.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isControlledAccess" class="member-name-link"><code>isControlledAccess</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Controlled access roads are roads with limited entrances and exits that allow uninterrupted high-speed traffic flow.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isDirtRoad" class="member-name-link"><code>isDirtRoad</code></a>

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isDividedRoad" class="member-name-link"><code>isDividedRoad</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates if there is a physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isNoThrough" class="member-name-link"><code>isNoThrough</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Identifies a no through road.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isPrivate" class="member-name-link"><code>isPrivate</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Private identifies roads that are not maintained by an organization responsible for maintenance of public roads.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRamp" class="member-name-link"><code>isRamp</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Range is a ramp: connects roads that do not intersect at grade.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRightDrivingSide" class="member-name-link"><code>isRightDrivingSide</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRoundabout" class="member-name-link"><code>isRoundabout</code></a>

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isTollway" class="member-name-link"><code>isTollway</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Identifies a road for which a fee must be paid to use the road.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isTunnel" class="member-name-link"><code>isTunnel</code></a>

  </div>

  <div class="col-last odd-row-color">

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

      RoadAttributes ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  - <div id="sdk-for-android-navigate-isRamp" class="section detail">

    ### isRamp

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRamp</span>

    </div>

    <div class="block">

    Range is a ramp: connects roads that do not intersect at grade. Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”) and for route guidance when determining if sign text should be used.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isControlledAccess" class="section detail">

    ### isControlledAccess

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isControlledAccess</span>

    </div>

    <div class="block">

    Controlled access roads are roads with limited entrances and exits that allow uninterrupted high-speed traffic flow. For example, the Interstate/Freeway network in the United States or the Motorway network in Europe. Controlled Access can be used for map display, avoidance of freeway/motorway, publishing speed limits, and route guidance timing.

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

  - <div id="sdk-for-android-navigate-isNoThrough" class="section detail">

    ### isNoThrough

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNoThrough</span>

    </div>

    <div class="block">

    Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isTollway" class="section detail">

    ### isTollway

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTollway</span>

    </div>

    <div class="block">

    Identifies a road for which a fee must be paid to use the road. Tollway may be used for map display (e.g., different rendering of toll roads) and routing. Tollway is flagged on roads that require a fee for traversal.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isDividedRoad" class="section detail">

    ### isDividedRoad

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDividedRoad</span>

    </div>

    <div class="block">

    Indicates if there is a physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-isRightDrivingSide" class="section detail">

    ### isRightDrivingSide

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRightDrivingSide</span>

    </div>

    <div class="block">

    Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side. For example, in New York it is always true and in London always false as the United Kingdom is a left-hand driving country.

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

  - <div id="sdk-for-android-navigate-isBuiltUpArea" class="section detail">

    ### isBuiltUpArea

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBuiltUpArea</span>

    </div>

    <div class="block">

    Indicates if the navigable segment is a built up area.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### RoadAttributes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoadAttributes</span>()

    </div>

    <div class="block">

    Creates a new instance.

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

