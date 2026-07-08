---
title: "MapSceneLights.Direction (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.MapSceneLights.Direction → com.here.sdk.mapview.MapSceneLights.Direction

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
[MapSceneLights](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">MapSceneLights.Direction</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The direction of lights as a pair of azimuth and altitude angles. See https://en.wikipedia.org/wiki/Horizontal_coordinate_system

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

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction#altitude" class="member-name-link"><code>altitude</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Direction altitude value in degrees in the range \[0, 90\].

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction#azimuth" class="member-name-link"><code>azimuth</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Direction azimuth value in degrees in the range \[0, 360).

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

      Direction ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Direction (double azimuth,
       double altitude)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a Direction from the values.

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

  - <div id="sdk-for-android-explore-azimuth" class="section detail">

    ### azimuth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">azimuth</span>

    </div>

    <div class="block">

    Direction azimuth value in degrees in the range \[0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.

    </div>

    </div>

  - <div id="sdk-for-android-explore-altitude" class="section detail">

    ### altitude

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">altitude</span>

    </div>

    <div class="block">

    Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### Direction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Direction</span>()

    </div>

    <div class="block">

    Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.

    </div>

    </div>

  - <div id="sdk-for-android-explore-init-double-double" class="section detail">

    ### Direction

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Direction</span><wbr></wbr><span class="parameters">(double azimuth, double altitude)</span>

    </div>

    <div class="block">

    Constructs a Direction from the values.

    </div>

    Parameters:  
    `azimuth` -

    Direction azimuth value in degrees in the range \[0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.

    `altitude` -

    Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

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

