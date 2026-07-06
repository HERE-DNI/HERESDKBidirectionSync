---
title: "MapMarker (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarker"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapMarker →
com.here.NativeBase → com.here.sdk.mapview.MapMarker

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapMarker</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

MapMarker is used to draw images on the map, for example to mark a
specific location. By default, the marker is centered on the given
geographic coordinates. Markers keep their size regardless of the
current zoom level of the map view. The image to be displayed is
represented by MapImage object. For performance reasons, it is highly
recommended to reuse a single instance of the image when creating
multiple identical markers. To display the map marker, it needs to be
added to the scene using
MapScene.addMapMarker(com.here.sdk.mapview.MapMarker) . To stop
displaying it, remove it from the scene using
MapScene.removeMapMarker(com.here.sdk.mapview.MapMarker) . The display
of a map marker is only guaranteed in case its origin is within the
viewport. At the moment, this is a known limitation that mostly affects
map markers which are visually large and cover a sizeable part of the
viewport. Note: Due to technical limitations using the MapMarkers API to
add a very large number of markers (several thousands, especially
10000+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and
lower frame rates. To work around this limitation the following approach
can be used: Register to map camera updates using
MapCamera.addListener(com.here.sdk.mapview.MapCameraListener) . Query
the bounding box of the camera viewport using MapCamera.getBoundingBox()
(it may be extended) and then use the method
GeoBox.contains(GeoCoordinates) in combination with
MapCamera.State.distanceToTargetInMeters to determine which MapMarkers
are actually visible to the user in the current camera viewport and thus
need to be added to the map.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-nested-class-summary"
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
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Styling options for the text of a MapMarker .

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
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

      MapMarker(GeoCoordinates coordinates,
       MapImage image)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of a marker at given coordinates, represented by
  specified image.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarker(GeoCoordinates coordinates,
       MapImage image,
       Anchor2D anchor)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates an instance of a marker at given coordinates, represented by
  specified image, with anchor point specifying how the image is
  positioned relative to the marker's coordinates.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapMarker(GeoCoordinates coordinates,
       MapImage image,
       String text)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a MapMarker instance at given coordinates with specified image
  and text and a default text style.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
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

      cancelAnimation(MapMarkerAnimation animation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Cancels single ongoing animation.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Anchor2D`](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAnchor()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets current anchor point for the marker image.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCoordinates()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the point on the map where the marker is drawn.

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

  Gets draw order of this marker relative to other markers.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFadeDuration()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current duration of a fade-in effect on marker addition to a
  scene or a fade-out effect on marker removal from a scene.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapImage`](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getImage()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets currently used map image.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Metadata`](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMetadata()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the Metadata instance attached to this marker.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOpacity()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current opacity of the marker image.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getText()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the text drawn on the map by the MapMarker .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMarker.TextStyle`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTextStyle()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a copy of the TextStyle currently in use by the MapMarker .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapMeasureRange`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVisibilityRanges()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of visibility ranges.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isOverlapAllowed()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns true if the marker allows overlap with other markers, false
  otherwise.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isTextOptional()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns true if the marker allows text to be hidden, false otherwise.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setAnchor(Anchor2D value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets anchor point of the marker image which specifies the position
  offset relative to the marker's coordinates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCoordinates(GeoCoordinates value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the point on the map where the marker is drawn.

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

  Sets draw order of this marker relative to other markers.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setFadeDuration(Duration value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets duration of a fade-in effect on marker addition to a scene or a
  fade-out effect on marker removal from a scene.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setImage(MapImage value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets map image used to represent the marker on screen.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMetadata(Metadata value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the Metadata instance attached to this marker.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOpacity(double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the opacity of the marker image.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOverlapAllowed(boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether the marker is allowed to overlap with other markers.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setText(String value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the text to be drawn on the map by the MapMarker .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTextOptional(boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets whether the marker is allowed to appear without text.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTextStyle(MapMarker.TextStyle value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the TextStyle to be used by the MapMarker .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVisibilityRanges(List<MapMeasureRange> value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets visibility ranges for this map marker.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      startAnimation(MapMarkerAnimation animation,
       AnimationListener animationListener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts animation of this map marker according to provided
  MapMarkerAnimation .

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
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### MapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image)</span>

    </div>

    <div class="block">

    Creates an instance of a marker at given coordinates, represented by
    specified image. The altitude component of the coordinates is
    ignored.

    </div>

    Parameters:  
    `coordinates` -

    The marker's geographical coordinates.

    `image` -

    The image to draw on the map.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,java.lang.String)"
    class="section detail">

    ### MapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> text)</span>

    </div>

    <div class="block">

    Creates a MapMarker instance at given coordinates with specified
    image and text and a default text style. The altitude component of
    the coordinates is ignored.

    </div>

    Parameters:  
    `coordinates` -

    The marker's geographical coordinates.

    `image` -

    The image to draw on the map.

    `text` -

    The text to draw on the map.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### MapMarker

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image,
    @NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") anchor)</span>

    </div>

    <div class="block">

    Creates an instance of a marker at given coordinates, represented by
    specified image, with anchor point specifying how the image is
    positioned relative to the marker's coordinates. The anchor is a way
    of specifying position offset relative to image's dimensions on the
    screen. For example, (0, 0) places the top-left corner of the image
    at the marker's coordinates. (1, 1) would place the bottom-right
    corner of the image at the marker's coordinates. (0.5, 0.5) which is
    the default value would center the image at the marker's
    coordinates. Values outside the 0..1 range are also allowed, for
    example (0.5, 2) would display the image centered horizontally with
    its bottom edge above the marker's coordinates at the distance in
    pixels that is equal to the height of the image.

    </div>

    Parameters:  
    `coordinates` -

    The marker's geographical coordinates.

    `image` -

    The image to draw on the map.

    `anchor` -

    The anchor point for the marker image which specifies the position
    offset relative to the marker's coordinates.

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-startAnimation(com.here.sdk.animation.MapMarkerAnimation,com.here.sdk.animation.AnimationListener)"
    class="section detail">

    ### startAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAnimation</span><span class="parameters">(@NonNull
    [MapMarkerAnimation](sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation "class in com.here.sdk.animation") animation,
    @Nullable
    [AnimationListener](sdk-for-android-explore-com-here-sdk-animation-animationlistener "interface in com.here.sdk.animation") animationListener)</span>

    </div>

    <div class="block">

    Starts animation of this map marker according to provided
    MapMarkerAnimation . The MapMarkerAnimation may be shared between
    multiple instances of MapMarker . Starting animation on one map
    marker does not influence any ongoing animations on other map
    markers. Any ongoing animation of this marker instance will get
    cancelled.

    </div>

    Parameters:  
    `animation` -

    The animation to start, may be used for multiple different map
    markers.

    `animationListener` -

    The listener to receive notifications about animation start,
    completion or cancellation.

    </div>
<div id="sdk-for-android-explore-cancelAnimation(com.here.sdk.animation.MapMarkerAnimation)"
    class="section detail">

    ### cancelAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelAnimation</span><span class="parameters">(@NonNull
    [MapMarkerAnimation](sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation "class in com.here.sdk.animation") animation)</span>

    </div>

    <div class="block">

    Cancels single ongoing animation. Does nothing if animation was not
    started for this map marker. Does not cancel other animations if the
    same MapMarkerAnimation object was applied to multiple MapMarker s.

    </div>

    Parameters:  
    `animation` -

    The animation to cancel.

    </div>
<div id="sdk-for-android-explore-getCoordinates()"
    class="section detail">

    ### getCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getCoordinates</span>()

    </div>

    <div class="block">

    Gets the point on the map where the marker is drawn.

    </div>

    Returns:  
    The point on the map where the map marker is drawn.

    </div>
<div id="sdk-for-android-explore-setCoordinates(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### setCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCoordinates</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the point on the map where the marker is drawn. The altitude
    component of the coordinates is ignored.

    </div>

    Parameters:  
    `value` -

    The point on the map where the map marker is drawn.

    </div>
<div id="sdk-for-android-explore-getMetadata()"
    class="section detail">

    ### getMetadata

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")</span> <span class="element-name">getMetadata</span>()

    </div>

    <div class="block">

    Gets the Metadata instance attached to this marker. This will be
    null if nothing has been attached before.

    </div>

    Returns:  
    The Metadata instance attached to this marker, see
    [`Metadata`](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core").

    </div>
<div id="sdk-for-android-explore-setMetadata(com.here.sdk.core.Metadata)"
    class="section detail">

    ### setMetadata

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><span class="parameters">(@Nullable
    [Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the Metadata instance attached to this marker.

    </div>

    Parameters:  
    `value` -

    The Metadata instance attached to this marker, see
    [`Metadata`](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core").

    </div>
<div id="sdk-for-android-explore-isOverlapAllowed()"
    class="section detail">

    ### isOverlapAllowed

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOverlapAllowed</span>()

    </div>

    <div class="block">

    Returns true if the marker allows overlap with other markers, false
    otherwise. Defaults to true .

    </div>

    Returns:  
    Determines whether or not the marker can overlap other markers.

    </div>
<div id="sdk-for-android-explore-setOverlapAllowed(boolean)"
    class="section detail">

    ### setOverlapAllowed

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOverlapAllowed</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether the marker is allowed to overlap with other markers. If
    false , it will disappear the moment it overlaps another marker that
    has a higher visibility priority. A marker that allows overlap will
    always be drawn. Among markers that don't allow overlap, the one
    with the highest draw order has priority. Marker that is hidden due
    to overlapping with other markers is not pickable.

    </div>

    Parameters:  
    `value` -

    Determines whether or not the marker can overlap other markers.

    </div>
<div id="sdk-for-android-explore-isTextOptional()"
    class="section detail">

    ### isTextOptional

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTextOptional</span>()

    </div>

    <div class="block">

    Returns true if the marker allows text to be hidden, false
    otherwise. Defaults to false .

    </div>

    Returns:  
    Determines if the marker can be displayed with icon and without
    text.

    </div>
<div id="sdk-for-android-explore-setTextOptional(boolean)"
    class="section detail">

    ### setTextOptional

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTextOptional</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets whether the marker is allowed to appear without text. Controls
    whenever MapMarker can be shown as icon only when isOverlapAllowed()
    is false , has no effect otherwise. If false then the MapMarker will
    not appear when icon or text are blocked by other labels. If true ,
    icon will appear even if the text part is blocked by other labels.

    </div>

    Parameters:  
    `value` -

    Determines if the marker can be displayed with icon and without
    text.

    </div>
<div id="sdk-for-android-explore-getDrawOrder()"
    class="section detail">

    ### getDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()

    </div>

    <div class="block">

    Gets draw order of this marker relative to other markers. The
    default value is 0.

    </div>

    Returns:  
    The draw order of this marker relative to other markers.

    </div>
<div id="sdk-for-android-explore-setDrawOrder(int)"
    class="section detail">

    ### setDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets draw order of this marker relative to other markers. Markers
    with higher draw order value are drawn on top of markers with lower
    draw order. In case multiple markers have the same draw order value
    then the order in which they were added to the scene matters. Last
    added marker is drawn on top. Allowed range is \[0, 1023\]. Values
    outside this range will be clamped. The default value is 0.

    </div>

    Parameters:  
    `value` -

    The draw order of this marker relative to other markers.

    </div>
<div id="sdk-for-android-explore-getImage()" class="section detail">

    ### getImage

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">getImage</span>()

    </div>

    <div class="block">

    Gets currently used map image.

    </div>

    Returns:  
    Image representing the marker on the screen.

    </div>
<div id="sdk-for-android-explore-setImage(com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### setImage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImage</span><span class="parameters">(@NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets map image used to represent the marker on screen.

    </div>

    Parameters:  
    `value` -

    Image representing the marker on the screen.

    </div>
<div id="sdk-for-android-explore-getAnchor()"
    class="section detail">

    ### getAnchor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")</span> <span class="element-name">getAnchor</span>()

    </div>

    <div class="block">

    Gets current anchor point for the marker image.

    </div>

    Returns:  
    The anchor point for the marker image which specifies the position
    offset relative to the marker's coordinates.

    </div>
<div id="sdk-for-android-explore-setAnchor(com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### setAnchor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnchor</span><span class="parameters">(@NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets anchor point of the marker image which specifies the position
    offset relative to the marker's coordinates. For example, (0, 0)
    places the top-left corner of the image at the marker's coordinates.
    (1, 1) would place the bottom-right corner of the image at the
    marker's coordinates. (0.5, 0.5) which is the default value would
    center the image at the marker's coordinates. Values outside the
    0..1 range are also allowed, for example (0.5, 2) would display the
    image centered horizontally with its bottom edge above the marker's
    coordinates at the distance in pixels that is equal to the height of
    the image.

    </div>

    Parameters:  
    `value` -

    The anchor point for the marker image which specifies the position
    offset relative to the marker's coordinates.

    </div>
<div id="sdk-for-android-explore-getOpacity()"
    class="section detail">

    ### getOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()

    </div>

    <div class="block">

    Gets the current opacity of the marker image. Value is in the range
    of \[0.0, 1.0\]. Default value is 1.0.

    </div>

    Returns:  
    Opacity, the factor applied to the alpha channel of the marker
    image.

    </div>
<div id="sdk-for-android-explore-setOpacity(double)"
    class="section detail">

    ### setOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the opacity of the marker image. Provided value is clamped to
    the range of \[0.0, 1.0\]. Default value is 1.0, which means marker
    is displayed with the default opacity of the image. Markers with
    opacity value set to 0.0 are still on the map and are considered for
    picking.

    </div>

    Parameters:  
    `value` -

    Opacity, the factor applied to the alpha channel of the marker
    image.

    </div>
<div id="sdk-for-android-explore-getFadeDuration()"
    class="section detail">

    ### getFadeDuration

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getFadeDuration</span>()

    </div>

    <div class="block">

    Gets the current duration of a fade-in effect on marker addition to
    a scene or a fade-out effect on marker removal from a scene.

    </div>

    Returns:  
    Duration of a fade-in effect on marker addition to a scene or a
    fade-out effect on marker removal from a scene.

    </div>
<div id="sdk-for-android-explore-setFadeDuration(com.here.time.Duration)"
    class="section detail">

    ### setFadeDuration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFadeDuration</span><span class="parameters">(@NonNull
    [Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") value)</span>

    </div>

    <div class="block">

    Sets duration of a fade-in effect on marker addition to a scene or a
    fade-out effect on marker removal from a scene. Provided value is
    clamped in range \[0.0, 10.0\] seconds. Default value is 0 seconds
    which means the effect is disabled and marker is added/removed
    immediately without any animation. Fade-in effect is also applied
    when marker leaves and then re-enters screen area. Change to this
    property is made asynchronously and is not guaranteed to take effect
    on the next rendered frame. In particular, changing fade duration
    and removing the marker immediately after may result in the new
    value being ignored for this removal.

    </div>

    Parameters:  
    `value` -

    Duration of a fade-in effect on marker addition to a scene or a
    fade-out effect on marker removal from a scene.

    </div>
<div id="sdk-for-android-explore-getText()" class="section detail">

    ### getText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()

    </div>

    <div class="block">

    Gets the text drawn on the map by the MapMarker .

    </div>

    Returns:  
    The text to be drawn on the map along with the image of the
    `MapMarker`.

    </div>
<div id="sdk-for-android-explore-setText(java.lang.String)"
    class="section detail">

    ### setText

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets the text to be drawn on the map by the MapMarker .

    </div>

    Parameters:  
    `value` -

    The text to be drawn on the map along with the image of the
    `MapMarker`.

    </div>
<div id="sdk-for-android-explore-getTextStyle()"
    class="section detail">

    ### getTextStyle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMarker.TextStyle](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle "class in com.here.sdk.mapview")</span> <span class="element-name">getTextStyle</span>()

    </div>

    <div class="block">

    Gets a copy of the TextStyle currently in use by the MapMarker .

    </div>

    Returns:  
    The `TextStyle` applied to the text of the `MapMarker`.

    </div>
<div id="sdk-for-android-explore-setTextStyle(com.here.sdk.mapview.MapMarker.TextStyle)"
    class="section detail">

    ### setTextStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTextStyle</span><span class="parameters">(@NonNull
    [MapMarker.TextStyle](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle "class in com.here.sdk.mapview") value)</span>

    </div>

    <div class="block">

    Sets the TextStyle to be used by the MapMarker .

    </div>

    Parameters:  
    `value` -

    The `TextStyle` applied to the text of the `MapMarker`.

    </div>
<div id="sdk-for-android-explore-getVisibilityRanges()"
    class="section detail">

    ### getVisibilityRanges

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")></span> <span class="element-name">getVisibilityRanges</span>()

    </div>

    <div class="block">

    Gets the list of visibility ranges. The map marker is visible only
    inside these map measure ranges. When empty (the default), the map
    marker is visible without map measure restrictions.

    </div>

    Returns:  
    The list of visibility ranges. The map marker is visible only inside
    these map measure ranges.

    </div>
<div id="sdk-for-android-explore-setVisibilityRanges(java.util.List)"
    class="section detail">

    ### setVisibilityRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMeasureRange](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")> value)</span>

    </div>

    <div class="block">

    Sets visibility ranges for this map marker. A range is half open -
    \[minimumZoomLevel, maximumZoomLevel), the given maximum value is
    not contained in the range. The map marker is visible only inside
    these map measure ranges. When empty (the default), the map marker
    is visible without map measure restrictions. Only
    MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are
    supported. MapMeasureRange (s) of other unsupported types will be
    ignored.

    </div>

    Parameters:  
    `value` -

    The list of visibility ranges. The map marker is visible only inside
    these map measure ranges.

    </div>

  </div>

</div>

