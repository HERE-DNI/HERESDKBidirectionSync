---
title: "MapImageOverlay (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapimageoverlay"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapImageOverlay →
com.here.NativeBase → com.here.sdk.mapview.MapImageOverlay

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapImageOverlay</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

MapImageOverlay is used to draw images over the map, at a view
coordinate inside the map viewport. The image to be displayed is
represented by a MapImage object. By default, the overlay is centered on
the given view coordinate. The resulting viewport area covered by the
overlay is computed out of the overlay's view coordinate, the anchor
point and the image size. The overlay subareas that fall outside of the
map viewport get clipped. To display the map overlay, it needs to be
added to the scene using
MapScene.addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay) . To
stop displaying it, remove it from the scene using
MapScene.removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay) .

</div>

</div>

<div class="section summary">

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

      MapImageOverlay(Point2D viewCoordinates,
       MapImage image)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of an overlay at given view coordinates,
  represented by specified image.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapImageOverlay(Point2D viewCoordinates,
       MapImage image,
       Anchor2D anchor)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates an instance of an overlay at given view coordinates,
  represented by specified image, with anchor point specifying how the
  image is positioned relative to the overlay's view coordinates.

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

  [`Anchor2D`](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAnchor()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets current anchor point for the overlay image.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawOrder()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets draw order of this MapImageOverlay .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapImage`](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getImage()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets currently used map image.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Point2D`](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getViewCoordinates()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the view point in pixels on the map viewport where the overlay is
  drawn.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setAnchor(Anchor2D value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets anchor point of the overlay image which specifies the position
  offset relative to the overlay's view coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDrawOrder(int value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets draw order of this MapImageOverlay .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setImage(MapImage value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the image overlayed on map.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setViewCoordinates(Point2D value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the view point in pixels on the map viewport where the overlay is
  drawn.

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

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### MapImageOverlay

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapImageOverlay</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") viewCoordinates,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image)</span>

    </div>

    <div class="block">

    Creates an instance of an overlay at given view coordinates,
    represented by specified image.

    </div>

    Parameters:  
    `viewCoordinates` -

    The overlay's view coordinates in pixels.

    `image` -

    The image to draw on the map.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### MapImageOverlay

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapImageOverlay</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") viewCoordinates,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image,
    @NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") anchor)</span>

    </div>

    <div class="block">

    Creates an instance of an overlay at given view coordinates,
    represented by specified image, with anchor point specifying how the
    image is positioned relative to the overlay's view coordinates. The
    anchor is a way of specifying position offset relative to image's
    dimensions on the view. For example, (0, 0) places the top-left
    corner of the image at the overlay's view coordinates. (1, 1) would
    place the bottom-right corner of the image at the overlay's view
    coordinates. (0.5, 0.5) which is the default value would center the
    image at the overlay's view coordinates. Values outside the 0..1
    range are also allowed, for example (0.5, 2) would display the image
    centered horizontally with its bottom edge above the overlay's view
    coordinates at the distance in pixels that is equal to the height of
    the image.

    </div>

    Parameters:  
    `viewCoordinates` -

    The overlay's view coordinates in pixels.

    `image` -

    The image to draw on the map.

    `anchor` -

    The anchor point for the overlay image which specifies the position
    offset relative to the overlay's view coordinates.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getViewCoordinates()"
    class="section detail">

    ### getViewCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")</span> <span class="element-name">getViewCoordinates</span>()

    </div>

    <div class="block">

    Gets the view point in pixels on the map viewport where the overlay
    is drawn.

    </div>

    Returns:  
    The view point in pixels on the map viewport where the map overlay
    is drawn.

    </div>

  - <div id="sdk-for-android-explore-setViewCoordinates(com.here.sdk.core.Point2D)"
    class="section detail">

    ### setViewCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViewCoordinates</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the view point in pixels on the map viewport where the overlay
    is drawn.

    </div>

    Parameters:  
    `value` -

    The view point in pixels on the map viewport where the map overlay
    is drawn.

    </div>

  - <div id="sdk-for-android-explore-getDrawOrder()"
    class="section detail">

    ### getDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()

    </div>

    <div class="block">

    Gets draw order of this MapImageOverlay . The default value is 0.

    </div>

    Returns:  
    Draw order of this `MapImageOverlay`.

    </div>

  - <div id="sdk-for-android-explore-setDrawOrder(int)"
    class="section detail">

    ### setDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets draw order of this MapImageOverlay . Overlays with higher draw
    order value are drawn on top of overlays with lower draw order. In
    case multiple overlays have the same draw order value then the order
    in which they were added to the scene matters. Last added overlay is
    drawn on top. Allowed range is \[0, 1023\]. Values outside this
    range will be clamped.

    </div>

    Parameters:  
    `value` -

    Draw order of this `MapImageOverlay`.

    </div>

  - <div id="sdk-for-android-explore-getImage()" class="section detail">

    ### getImage

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">getImage</span>()

    </div>

    <div class="block">

    Gets currently used map image.

    </div>

    Returns:  
    Image overlayed on the map.

    </div>

  - <div id="sdk-for-android-explore-setImage(com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### setImage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImage</span><span class="parameters">(@NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets the image overlayed on map.

    </div>

    Parameters:  
    `value` -

    Image overlayed on the map.

    </div>

  - <div id="sdk-for-android-explore-getAnchor()"
    class="section detail">

    ### getAnchor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")</span> <span class="element-name">getAnchor</span>()

    </div>

    <div class="block">

    Gets current anchor point for the overlay image.

    </div>

    Returns:  
    The anchor point for the overlay image which specifies the position
    offset relative to the overlay's view coordinates.

    </div>

  - <div id="sdk-for-android-explore-setAnchor(com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### setAnchor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnchor</span><span class="parameters">(@NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets anchor point of the overlay image which specifies the position
    offset relative to the overlay's view coordinates. For example,
    (0, 0) places the top-left corner of the image at the overlay's view
    coordinates. (1, 1) would place the bottom-right corner of the image
    at the overlay's view coordinates. (0.5, 0.5) which is the default
    value would center the image at the overlay's view coordinates.
    Values outside the 0..1 range are also allowed, for example (0.5, 2)
    would display the image centered horizontally with its bottom edge
    above the overlay's view coordinates at the distance in pixels that
    is equal to the height of the image.

    </div>

    Parameters:  
    `value` -

    The anchor point for the overlay image which specifies the position
    offset relative to the overlay's view coordinates.

    </div>

  </div>

</div>

