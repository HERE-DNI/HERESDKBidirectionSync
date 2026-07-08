---
title: "MapPolyline (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapPolyline →
com.here.NativeBase com.here.sdk.mapview.MapPolyline →
com.here.sdk.mapview.MapPolyline

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapPolyline</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A visual representation of a line on the map. The geometry to be
visualized is represented by an instance of GeoPolyline . Altitude
component of GeoPolyline 's vertices is ignored.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashimagerepresentation"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapPolyline.DashImageRepresentation</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents a dash pattern for the map polyline consisting of images
  rendered with certain gaps from each other.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashrepresentation"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapPolyline.DashRepresentation</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Represents a dash pattern for map polyline where the dash can be
  rendered as a colored line and the gap can be either empty or colored.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Base class to represent the visual appearance of a MapPolyline .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapPolyline.SolidMultiColorRepresentation</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Representation allows map polyline to be colored in multiple specified
  color segments.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidrepresentation"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapPolyline.SolidRepresentation</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Representation for a solid line without outline.

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

      MapPolyline ( GeoPolyline geometry, MapPolyline.Representation representation)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new MapPolyline instance with a specified visual
  representation.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      cancelAnimation ( MapPolylineAnimation animation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Cancels single ongoing animation of this map polyline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawOrder ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the draw order of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`DrawOrderType`](sdk-for-android-explore-com-here-sdk-mapview-drawordertype "enum class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawOrderType ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the draw order type of the polyline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometry ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the geometry of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapContentCategory`](sdk-for-android-explore-com-here-sdk-mapview-mapcontentcategory "enum class in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMapContentCategoriesToBlock ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets list of map content categories this polyline should block.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Metadata`](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMetadata ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the Metadata instance attached to this polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getProgress ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the progress of the polyline, 0 by default.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getProgressColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the progress color of the polyline, opaque white by default.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getProgressGradientLength ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the maximum gradient length between MapPolyline.lineColor' and
  'MapPolyline.progressColor in zoom level dependent pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getProgressOutlineColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the progress outline color of the polyline, opaque white by
  default.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapMeasureRange`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVisibilityRanges ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of visibility ranges.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDrawOrder (int value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the draw order of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDrawOrderType ( DrawOrderType value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the draw order type of the polyline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setGeometry ( GeoPolyline value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the geometry of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMapContentCategoriesToBlock ( List < MapContentCategory > value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets list of map content categories this polyline should block.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMetadata ( Metadata value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the Metadata instance attached to this polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setProgress (double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the progress of the polyline from its starting point as a ratio
  of its total length clamped to the range \[0; 1\].

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setProgressColor ( Color value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the progress color of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setProgressGradientLength ( MapMeasureDependentRenderSize value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the maximum gradient length between MapPolyline.lineColor' and
  'MapPolyline.progressColor in zoom level dependent pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setProgressOutlineColor ( Color value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the progress outline color of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRepresentation ( MapPolyline.Representation representation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Changes the appearance of the MapPolyline instance.

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

  Sets visibility ranges for this map polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      startAnimation ( MapPolylineAnimation animation, AnimationListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts an animation of this map polyline.

  </div>

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
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

<!-- -->

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoPolyline-com-here-sdk-mapview-MapPolyline-Representation"
    class="section detail">

    ### MapPolyline

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapPolyline</span><span class="parameters">(@NonNull
    [GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core") geometry,
    @NonNull
    [MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview") representation)</span>

    </div>

    <div class="block">

    Creates a new MapPolyline instance with a specified visual
    representation. Altitude component of GeoPolyline 's vertices is
    ignored. After creating a MapPolyline with this representation, the
    deprecated MapPolyline properties do not work and any change to them
    will be ignored. Any modifications to polyline's appearance must be
    done with
    setRepresentation(com.here.sdk.mapview.MapPolyline.Representation) .

    </div>

    Parameters:  
    `geometry` -

    The list of vertices representing the polyline.

    `representation` -

    The styling properties of the polyline.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-setRepresentation-com-here-sdk-mapview-MapPolyline-Representation"
    class="section detail">

    ### setRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRepresentation</span><span class="parameters">(@NonNull
    [MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview") representation)</span>

    </div>

    <div class="block">

    Changes the appearance of the MapPolyline instance.

    </div>

    Parameters:  
    `representation` -

    The representation describing a new appearance of the `MapPolyline`.

    </div>

  - <div id="sdk-for-android-explore-startAnimation-com-here-sdk-animation-MapPolylineAnimation-com-here-sdk-animation-AnimationListener"
    class="section detail">

    ### startAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAnimation</span><span class="parameters">(@NonNull
    [MapPolylineAnimation](sdk-for-android-explore-com-here-sdk-animation-mappolylineanimation "class in com.here.sdk.animation") animation,
    @NonNull
    [AnimationListener](sdk-for-android-explore-com-here-sdk-animation-animationlistener "interface in com.here.sdk.animation") listener)</span>

    </div>

    <div class="block">

    Starts an animation of this map polyline. The MapPolylineAnimation
    may be shared between multiple instances of MapPolyline . Starting
    animation on one polyline does not influence any ongoing animations
    on other polylines. Any ongoing animation of this map polyline will
    get cancelled.

    </div>

    Parameters:  
    `animation` -

    The animation to start.

    `listener` -

    The listener to receive notifications about animation start,
    completion or cancellation.

    </div>

  - <div id="sdk-for-android-explore-cancelAnimation-com-here-sdk-animation-MapPolylineAnimation"
    class="section detail">

    ### cancelAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelAnimation</span><span class="parameters">(@NonNull
    [MapPolylineAnimation](sdk-for-android-explore-com-here-sdk-animation-mappolylineanimation "class in com.here.sdk.animation") animation)</span>

    </div>

    <div class="block">

    Cancels single ongoing animation of this map polyline. Does nothing
    if the specified animation is not currently in progress for this
    polyline. Does not affect other polylines that might be running this
    animation.

    </div>

    Parameters:  
    `animation` -

    The animation to cancel

    </div>

  - <div id="sdk-for-android-explore-getGeometry"
    class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")</span> <span class="element-name">getGeometry</span>()

    </div>

    <div class="block">

    Gets the geometry of the polyline.

    </div>

    Returns:  
    The list of vertices that represent the geometry of the polyline.

    </div>

  - <div id="sdk-for-android-explore-setGeometry-com-here-sdk-core-GeoPolyline"
    class="section detail">

    ### setGeometry

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeometry</span><span class="parameters">(@NonNull
    [GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the geometry of the polyline. Altitude component of GeoPolyline
    's vertices is ignored.

    </div>

    Parameters:  
    `value` -

    The list of vertices that represent the geometry of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getMetadata"
    class="section detail">

    ### getMetadata

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")</span> <span class="element-name">getMetadata</span>()

    </div>

    <div class="block">

    Gets the Metadata instance attached to this polyline. This will be
    null if nothing has been attached before.

    </div>

    Returns:  
    The `Metadata` instance attached to this polyline.

    </div>

  - <div id="sdk-for-android-explore-setMetadata-com-here-sdk-core-Metadata"
    class="section detail">

    ### setMetadata

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><span class="parameters">(@Nullable
    [Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the Metadata instance attached to this polyline.

    </div>

    Parameters:  
    `value` -

    The `Metadata` instance attached to this polyline.

    </div>

  - <div id="sdk-for-android-explore-getDrawOrder"
    class="section detail">

    ### getDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()

    </div>

    <div class="block">

    Gets the draw order of the polyline. The default draw order is 0.

    </div>

    Returns:  
    The draw order of the polyline.

    </div>

  - <div id="sdk-for-android-explore-setDrawOrder-int"
    class="section detail">

    ### setDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets the draw order of the polyline. Polylines with a higher draw
    order are drawn on top of polylines with a lower draw order. In case
    multiple polylines have the same draw order, they can be rendered in
    different ways depending on the getDrawOrderType() set. Supplied
    value is clamped to the range \[0; 1023\].

    </div>

    Parameters:  
    `value` -

    The draw order of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getDrawOrderType"
    class="section detail">

    ### getDrawOrderType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DrawOrderType](sdk-for-android-explore-com-here-sdk-mapview-drawordertype "enum class in com.here.sdk.mapview")</span> <span class="element-name">getDrawOrderType</span>()

    </div>

    <div class="block">

    Gets the draw order type of the polyline. The default value is
    DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT .

    </div>

    Returns:  
    The draw order type of the polyline.

    </div>

  - <div id="sdk-for-android-explore-setDrawOrderType-com-here-sdk-mapview-DrawOrderType"
    class="section detail">

    ### setDrawOrderType

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrderType</span><span class="parameters">(@NonNull
    [DrawOrderType](sdk-for-android-explore-com-here-sdk-mapview-drawordertype "enum class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets the draw order type of the polyline. For
    DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT , map polylines
    with outlines having the same draw order are drawn as a whole in the
    order of addition to a map scene. There is no possibility that parts
    of another polyline, regardless of its draw order value, are drawn
    between outline and mainline of another polyline. With
    DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT , polylines are
    rendered one by one. For
    DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT , for multiple
    polylines with outlines having the same draw order, all outlines are
    rendered first in an arbitrary order and then all mainlines are
    drawn on top of those polylines in an arbitrary order.
    DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT allows speeding
    up the rendering process and keeping high frame rates when many
    similar polylines (with same styling attributes and
    MapPolyline.Representation ) are present in a map scene.

    </div>

    Parameters:  
    `value` -

    The draw order type of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getVisibilityRanges"
    class="section detail">

    ### getVisibilityRanges

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")\></span> <span class="element-name">getVisibilityRanges</span>()

    </div>

    <div class="block">

    Gets the list of visibility ranges. The map polyline is visible only
    inside these map measure ranges. When empty (the default), the map
    polyline is visible without map measure restrictions.

    </div>

    Returns:  
    The list of visibility ranges. The map polyline is visible only
    inside these map measure ranges.

    </div>

  - <div id="sdk-for-android-explore-setVisibilityRanges-java-util-List"
    class="section detail">

    ### setVisibilityRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")\> value)</span>

    </div>

    <div class="block">

    Sets visibility ranges for this map polyline. A range is half open -
    \[minimumZoomLevel, maximumZoomLevel), the given maximum value is
    not contained in the range. The map polyline is visible only inside
    these map measure ranges. When empty (the default), the map polyline
    is visible without map measure restrictions. Only
    MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are
    supported. MapMeasureRange (s) of other unsupported types will be
    ignored.

    </div>

    Parameters:  
    `value` -

    The list of visibility ranges. The map polyline is visible only
    inside these map measure ranges.

    </div>

  - <div id="sdk-for-android-explore-getProgress"
    class="section detail">

    ### getProgress

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getProgress</span>()

    </div>

    <div class="block">

    Gets the progress of the polyline, 0 by default.

    </div>

    Returns:  
    The progress from the polyline's starting point, as a ratio of its
    total length clamped to the range \[0, 1\].

    </div>

  - <div id="sdk-for-android-explore-setProgress-double"
    class="section detail">

    ### setProgress

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgress</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the progress of the polyline from its starting point as a ratio
    of its total length clamped to the range \[0; 1\]. As the progress
    varies, the equivalent part of the polyline gets covered by the
    progress color and progress outline color. The rest of the polyline
    until its end point retains the line color and outline color along
    with an optional dash pattern.

    </div>

    Parameters:  
    `value` -

    The progress from the polyline's starting point, as a ratio of its
    total length clamped to the range \[0, 1\].

    </div>

  - <div id="sdk-for-android-explore-getProgressColor"
    class="section detail">

    ### getProgressColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getProgressColor</span>()

    </div>

    <div class="block">

    Gets the progress color of the polyline, opaque white by default.

    </div>

    Returns:  
    The color used for the progress part of the polyline.

    </div>

  - <div id="sdk-for-android-explore-setProgressColor-com-here-sdk-core-Color"
    class="section detail">

    ### setProgressColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgressColor</span><span class="parameters">(@NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the progress color of the polyline.

    </div>

    Parameters:  
    `value` -

    The color used for the progress part of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getProgressOutlineColor"
    class="section detail">

    ### getProgressOutlineColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getProgressOutlineColor</span>()

    </div>

    <div class="block">

    Gets the progress outline color of the polyline, opaque white by
    default.

    </div>

    Returns:  
    The color used for outline of the progress part of the polyline.

    </div>

  - <div id="sdk-for-android-explore-setProgressOutlineColor-com-here-sdk-core-Color"
    class="section detail">

    ### setProgressOutlineColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgressOutlineColor</span><span class="parameters">(@NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the progress outline color of the polyline.

    </div>

    Parameters:  
    `value` -

    The color used for outline of the progress part of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getProgressGradientLength"
    class="section detail">

    ### getProgressGradientLength

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getProgressGradientLength</span>()

    </div>

    <div class="block">

    Gets the maximum gradient length between MapPolyline.lineColor' and
    'MapPolyline.progressColor in zoom level dependent pixels.

    </div>

    Returns:  
    The maximum gradient length between
    `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom
    level dependent pixels.

    </div>

  - <div id="sdk-for-android-explore-setProgressGradientLength-com-here-sdk-mapview-MapMeasureDependentRenderSize"
    class="section detail">

    ### setProgressGradientLength

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgressGradientLength</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets the maximum gradient length between MapPolyline.lineColor' and
    'MapPolyline.progressColor in zoom level dependent pixels. To
    achieve a constant gradient length, use
    MapMeasureDependentRenderSize with a single value. To achieve a
    gradient length dependent on map zoom, use
    MapMeasureDependentRenderSize with multiple values. The default
    value is a constant gradient length of zero pixels. The gradient is
    guaranteed to fit into polyline, i.e. the actual gradient can be
    shorter then progressGradientLength . For MapMeasure.Kind only
    MapMeasure.Kind.ZOOM_LEVEL is supported. For RenderSize.Unit only
    RenderSize.Unit.PIXELS is supported. A parameter with unsupported
    values is ignored.

    </div>

    Parameters:  
    `value` -

    The maximum gradient length between
    `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom
    level dependent pixels.

    </div>

  - <div id="sdk-for-android-explore-getMapContentCategoriesToBlock"
    class="section detail">

    ### getMapContentCategoriesToBlock

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapContentCategory](sdk-for-android-explore-com-here-sdk-mapview-mapcontentcategory "enum class in com.here.sdk.mapview")\></span> <span class="element-name">getMapContentCategoriesToBlock</span>()

    </div>

    <div class="block">

    Gets list of map content categories this polyline should block.
    Default value is an empty list meaning none of the map categories
    will be blocked.

    </div>

    Returns:  
    List of map content categories this polyline should block.

    </div>

  - <div id="sdk-for-android-explore-setMapContentCategoriesToBlock-java-util-List"
    class="section detail">

    ### setMapContentCategoriesToBlock

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMapContentCategoriesToBlock</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapContentCategory](sdk-for-android-explore-com-here-sdk-mapview-mapcontentcategory "enum class in com.here.sdk.mapview")\> value)</span>

    </div>

    <div class="block">

    Sets list of map content categories this polyline should block. Map
    content categories overlapping the polyline geometry (progress and
    non-progress) will be discarded from being rendered. Duplicate
    entries will be ignored and will have no additional effect.

    </div>

    Parameters:  
    `value` -

    List of map content categories this polyline should block.

    </div>

  </div>

