---
title: "PointDataBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatabuilder"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.datasource.PointDataBuilder → com.here.NativeBase com.here.sdk.mapview.datasource.PointDataBuilder → com.here.sdk.mapview.datasource.PointDataBuilder

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">PointDataBuilder</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Builder of PointData instances. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

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

      PointDataBuilder ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a builder instance.

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

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">`PointData`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      build ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Builds an instance of PointData and resets the builder instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">`PointDataBuilder`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withAttributes ( DataAttributes attributes)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder with custom attributes for point to be created.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">`PointDataBuilder`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withCoordinates ( GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder with geodetic coordinates for point to be created.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### PointDataBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PointDataBuilder</span>()

    </div>

    <div class="block">

    Creates a builder instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-withCoordinates-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### withCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></span> <span class="element-name">withCoordinates</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span>

    </div>

    <div class="block">

    Configures the builder with geodetic coordinates for point to be created.

    </div>

    Parameters:  
    `coordinates` -

    Geodetic coordinates of the point. Altitude of coordinates is ignored.

    Returns:  
    The builder.

    </div>

  - <div id="sdk-for-android-navigate-withAttributes-com-here-sdk-mapview-datasource-DataAttributes" class="section detail">

    ### withAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatabuilder" title="class in com.here.sdk.mapview.datasource">PointDataBuilder</a></span> <span class="element-name">withAttributes</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</span>

    </div>

    <div class="block">

    Configures the builder with custom attributes for point to be created.

    </div>

    Parameters:  
    `attributes` -

    Custom data attributes to be associated with the point.

    Returns:  
    The builder.

    </div>

  - <div id="sdk-for-android-navigate-build" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">PointData</a></span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Builds an instance of PointData and resets the builder instance.

    </div>

    Returns:  
    Instance of <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdata" title="class in com.here.sdk.mapview.datasource">`PointData`</a> created with the configured parameters.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

