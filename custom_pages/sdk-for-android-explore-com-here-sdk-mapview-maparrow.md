---
title: "MapArrow (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-maparrow"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapArrow →
com.here.NativeBase → com.here.sdk.mapview.MapArrow

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapArrow</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A visual representation of an arrow on the map. It consists of a tail -
a polyline with an arbitrary number of points - and a head at its end.
The map arrows are only visible on zoom levels >= 13. Altitude
component of GeoPolyline 's vertices is ignored.

</div>

</div>

<div class="section summary">

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
  <td><pre><code>MapArrow(GeoPolyline geometry,
   double widthInPixels,
   Color color)</code></pre></td>
  <td><div class="block">
  Creates a new MapArrow instance.
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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasure"
  title="class in com.here.sdk.mapview"><code>MapMeasure</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>&gt;</code></td>
  <td><pre><code>getMeasureDependentTailWidth()</code></pre></td>
  <td><div class="block">
  Gets the MapMeasure dependent arrow tail width in pixels.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange"
  title="class in com.here.sdk.mapview"><code>MapMeasureRange</code></a><code>&gt;</code></td>
  <td><pre><code>getVisibilityRanges()</code></pre></td>
  <td><div class="block">
  Gets the list of visibility ranges.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setMeasureDependentTailWidth(Map&lt;MapMeasure,Double&gt; value)</code></pre></td>
  <td><div class="block">
  Sets the MapMeasure dependent arrow tail width in pixels.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setVisibilityRanges(List&lt;MapMeasureRange&gt; value)</code></pre></td>
  <td><div class="block">
  Sets visibility ranges for this map arrow.
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.GeoPolyline,double,com.here.sdk.core.Color)"
    class="section detail">

    ### MapArrow

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapArrow</span><span class="parameters">(@NonNull
    [GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core") geometry,
    double widthInPixels, @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color)</span>

    </div>

    <div class="block">

    Creates a new MapArrow instance. Altitude component of GeoPolyline
    's vertices is ignored.

    </div>

    Parameters:  
    `geometry` -

    The geometry of the arrow tail. The last coordinate in the list
    defines the position where the head of the arrow is located.

    `widthInPixels` -

    The width of the arrow tail in pixel. Negative values are clamped
    to 0. The tip is scaled accordingly.

    `color` -

    The color of the arrow. The alpha channel is ignored, the color is
    interpreted as fully opaque.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="getMeasureDependentTailWidth()" class="section detail">

    ### getMeasureDependentTailWidth

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><[MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview"),<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>></span> <span class="element-name">getMeasureDependentTailWidth</span>()

    </div>

    <div class="block">

    Gets the MapMeasure dependent arrow tail width in pixels. If tail
    width was configured without MapMeasure dependency, then
    measureDependentTailWidth contains single entry with measure 0 of
    type MapMeasure.Kind.ZOOM_LEVEL and width value equal to
    widthInPixels . Note: This is a beta release of this feature, so
    there could be a few bugs and unexpected behavior. Related APIs may
    change for new releases without a deprecation process.

    </div>

    Returns:  
    The width of the arrow tail in pixels, where the key is a
    [`MapMeasure`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview")
    and the value is a tail width in pixels at this
    [`MapMeasure`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview").

    </div>

  - <div id="setMeasureDependentTailWidth(java.util.Map)"
    class="section detail">

    ### setMeasureDependentTailWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMeasureDependentTailWidth</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><[MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview"),<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> value)</span>

    </div>

    <div class="block">

    Sets the MapMeasure dependent arrow tail width in pixels. The width
    values are linearly interpolated between nearest map entries. Width
    values for MapMeasure outside the map entries are kept constant,
    using the value of the largest/smallest key. Only MapMeasure of
    MapMeasure.Kind.ZOOM_LEVEL type is supported. Other MapMeasure types
    are unsupported and hence, will be ignored. Map with a single entry
    is equivalent to use of the widthInPixels value in the constructor,
    so a constant width setting, independent of camera. Empty input is
    ignored and existing width is maintained. The width values should be
    positive. Map entries with width values less than or equal to 0 are
    ignored. Note: This is a beta release of this feature, so there
    could be a few bugs and unexpected behavior. Related APIs may change
    for new releases without a deprecation process.

    </div>

    Parameters:  
    `value` -

    The width of the arrow tail in pixels, where the key is a
    [`MapMeasure`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview")
    and the value is a tail width in pixels at this
    [`MapMeasure`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview").

    </div>

  - <div id="getVisibilityRanges()" class="section detail">

    ### getVisibilityRanges

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")></span> <span class="element-name">getVisibilityRanges</span>()

    </div>

    <div class="block">

    Gets the list of visibility ranges. A range is half-open -
    \[minimumZoomLevel, maximumZoomLevel), the given maximum value is
    not contained in the range. When empty (the default), the map arrows
    are visible without map measure restrictions. Only
    MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are
    supported. MapMeasureRange (s) of other unsupported types will be
    ignored.}

    </div>

    Returns:  
    The list of visibility ranges, in which the map arrow is visible.

    </div>

  - <div id="setVisibilityRanges(java.util.List)"
    class="section detail">

    ### setVisibilityRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")> value)</span>

    </div>

    <div class="block">

    Sets visibility ranges for this map arrow. A range is half-open -
    \[minimumZoomLevel, maximumZoomLevel), the given maximum value is
    not contained in the range. When empty (the default), the map arrows
    are visible without map measure restrictions. Only
    MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are
    supported. MapMeasureRange (s) of other unsupported types will be
    ignored.}

    </div>

    Parameters:  
    `value` -

    The list of visibility ranges, in which the map arrow is visible.

    </div>

  </div>

</div>

