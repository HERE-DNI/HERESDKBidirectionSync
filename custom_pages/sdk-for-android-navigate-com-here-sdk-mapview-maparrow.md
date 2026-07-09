---
title: "MapArrow (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-maparrow"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapArrow → com.here.NativeBase com.here.sdk.mapview.MapArrow → com.here.sdk.mapview.MapArrow

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapArrow</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary number of points - and a head at its end. The map arrows are only visible on zoom levels \>= 13. Altitude component of GeoPolyline 's vertices is ignored.

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

      MapArrow ( GeoPolyline geometry,
       double widthInPixels, Color color)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new MapArrow instance.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMeasureDependentTailWidth ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the MapMeasure dependent arrow tail width in pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">`MapMeasureRange`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVisibilityRanges ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of visibility ranges.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMeasureDependentTailWidth ( Map < MapMeasure , Double > value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the MapMeasure dependent arrow tail width in pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVisibilityRanges ( List < MapMeasureRange > value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets visibility ranges for this map arrow.

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoPolyline-double-com-here-sdk-core-Color" class="section detail">

    ### MapArrow

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapArrow</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry, double widthInPixels, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span>

    </div>

    <div class="block">

    Creates a new MapArrow instance. Altitude component of GeoPolyline 's vertices is ignored.

    </div>

    Parameters:  
    `geometry` -

    The geometry of the arrow tail. The last coordinate in the list defines the position where the head of the arrow is located.

    `widthInPixels` -

    The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.

    `color` -

    The color of the arrow. The alpha channel is ignored, the color is interpreted as fully opaque.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getMeasureDependentTailWidth" class="section detail">

    ### getMeasureDependentTailWidth

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\></span> <span class="element-name">getMeasureDependentTailWidth</span>()

    </div>

    <div class="block">

    Gets the MapMeasure dependent arrow tail width in pixels. If tail width was configured without MapMeasure dependency, then measureDependentTailWidth contains single entry with measure 0 of type MapMeasure.Kind.ZOOM_LEVEL and width value equal to widthInPixels . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Returns:  
    The width of the arrow tail in pixels, where the key is a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a> and the value is a tail width in pixels at this <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setMeasureDependentTailWidth-java-util-Map" class="section detail">

    ### setMeasureDependentTailWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMeasureDependentTailWidth</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a>\> value)</span>

    </div>

    <div class="block">

    Sets the MapMeasure dependent arrow tail width in pixels. The width values are linearly interpolated between nearest map entries. Width values for MapMeasure outside the map entries are kept constant, using the value of the largest/smallest key. Only MapMeasure of MapMeasure.Kind.ZOOM_LEVEL type is supported. Other MapMeasure types are unsupported and hence, will be ignored. Map with a single entry is equivalent to use of the widthInPixels value in the constructor, so a constant width setting, independent of camera. Empty input is ignored and existing width is maintained. The width values should be positive. Map entries with width values less than or equal to 0 are ignored. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `value` -

    The width of the arrow tail in pixels, where the key is a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a> and the value is a tail width in pixels at this <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">`MapMeasure`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getVisibilityRanges" class="section detail">

    ### getVisibilityRanges

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>\></span> <span class="element-name">getVisibilityRanges</span>()

    </div>

    <div class="block">

    Gets the list of visibility ranges. A range is half-open - \<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range. When empty (the default), the map arrows are visible without map measure restrictions. Only MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are supported. MapMeasureRange (s) of other unsupported types will be ignored.}

    </div>

    Returns:  
    The list of visibility ranges, in which the map arrow is visible.

    </div>

  - <div id="sdk-for-android-navigate-setVisibilityRanges-java-util-List" class="section detail">

    ### setVisibilityRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[MapMeasureRange</a>\> value)</span>

    </div>

    <div class="block">

    Sets visibility ranges for this map arrow. A range is half-open - \[minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range. When empty (the default), the map arrows are visible without map measure restrictions. Only MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are supported. MapMeasureRange (s) of other unsupported types will be ignored.}

    </div>

    Parameters:  
    `value` -

    The list of visibility ranges, in which the map arrow is visible.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

