---
title: "MapMarker3D (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarker3d"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapMarker3D →
com.here.NativeBase → com.here.sdk.mapview.MapMarker3D

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapMarker3D</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a 3D shape drawn on the map at specified geodetic
coordinates. It can have a solid color or be textured, depending on the
data from MapMarker3DModel . By default, a 3D marker is drawn on top of
all map content, including 3D map elements like extruded buildings or 3D
landmarks. This can be changed by enabling depth check using
setDepthCheckEnabled(boolean) . The display of a 3D marker is only
guaranteed in case its origin is within the viewport. At the moment,
this is a known limitation that mostly affects a 3D marker that is
visually large and covers a sizeable part of the viewport. Two aspects
determine how big the MapMarker3D will be on the screen and how will it
behave when the map is zoomed in and out. The first, and most impactful
is RenderSize.Unit , which specifies how the vertex coordinates of the
3D model are interpreted. Most importantly, it specifies whether the 3D
model is placed in world or screen coordinate space.
RenderSize.Unit.METERS will make the 3D model use world coordinate
space, meaning that it will change size together with the map when it is
zoomed in and out. RenderSize.Unit.PIXELS makes the 3D model use screen
coordinate space, meaning that it will have constant size on the screen
regardless of how the map zoom changes. So a simple 10 by 10 (in model
space) rectangle will have a size of 10 by 10 pixels on the screen.
RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS is similar to pixels, but the
resulting size will take into account the pixel density of the display,
meaning that physical size on the screen will be approximately the same
regardless of the size or resolution of the display. The second aspect
that determines size of MapMarker3D is scale. It can be specified at
construction time and can be changed later at any time using
setScale(double) . A 3D marker can be moved around a map by updating its
coordinates using setCoordinates(com.here.sdk.core.GeoCoordinates) .
Altitude component of the coordinates, if set, controls 3D marker's
elevation above ground. If not set, the 3D marker is placed at ground
level. Its orientation is specified by bearing, pitch and roll and can
be changed by using setBearing(double) , setPitch(double) and
setRoll(double) . A flat marker is a special case of a 3D marker, where
the 3D shape being drawn is a simple textured rectangle. In essence it's
an image drawn "on the ground". Such 3D marker can be conveniently
created using MapMarker3D(GeoCoordinates, MapImage, double,
RenderSize.Unit) constructor. Of course, once created, it can be rotated
to face any direction.

</div>

</div>

<div class="section summary">
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

      MapMarker3D(GeoCoordinates at,
       MapImage image,
       double scale,
       RenderSize.Unit unit)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a flat marker from provided map image.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarker3D(GeoCoordinates at,
       MapMarker3DModel model)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates an instance of a 3D marker.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapMarker3D(GeoCoordinates at,
       MapMarker3DModel model,
       double scale)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of a 3D marker with scale factor.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMarker3D(GeoCoordinates at,
       MapMarker3DModel model,
       double scale,
       RenderSize.Unit unit)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new 3D marker at given world coordinates, using the supplied
  3D model.

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

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBearing()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the bearing of the 3D model in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCoordinates()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the 3D marker's position on the map corresponding to the origin
  of the 3D marker model coordinate system.

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

  Gets the Metadata instance attached to this 3D marker.

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

  Returns an opacity factor which specifies the translucency of a 3D map
  marker.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPitch()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the pitch of the 3D model in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoll()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the roll of the 3D model in degrees.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getScale()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the scale factor applied to the 3D model before rendering.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapMeasureRange`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasurerange "class in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVisibilityRanges()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of visibility ranges.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isDepthCheckEnabled()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns true if depth check is enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isRenderInternalsEnabled()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a flag indicating whether to render internal geometry of a 3D
  marker occluded by its front facing polygons.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setBearing(double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the bearing of the 3D model in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCoordinates(GeoCoordinates value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the 3D marker's position on the map corresponding to the origin
  of the 3D marker model coordinate system.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDepthCheckEnabled(boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Set whether the depth of the 3D marker's vertices is considered during
  rendering.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMetadata(Metadata value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the Metadata instance attached to this 3D marker.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOpacity(double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets an opacity factor which specifies the translucency of a 3D map
  marker.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPitch(double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the pitch of the 3D model in degrees.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRenderInternalsEnabled(boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a flag indicating whether to render internal geometry of a 3D
  marker occluded by its front facing polygons.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRoll(double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the roll of the 3D model in degrees.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setScale(double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the scale factor, to be applied to the 3D model before rendering.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVisibilityRanges(List<MapMeasureRange> value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets visibility ranges for this 3D marker.

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
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel)"
    class="section detail">

    ### MapMarker3D

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") at,
    @NonNull
    [MapMarker3DModel](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel "class in com.here.sdk.mapview") model)</span>

    </div>

    <div class="block">

    Creates an instance of a 3D marker. The origin of the 3D model's
    local coordinate system is placed at the specified geographical
    coordinates. Altitude component of the coordinates, if set, controls
    3D marker's elevation above ground. If not set, the 3D marker is
    placed at ground level.

    </div>

    Parameters:  
    `at` -

    The geographical coordinates where the 3D marker is placed
    corresponding to origin of the 3D model's local coordinate system.

    `model` -

    The 3D model used to draw 3D marker.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,double,com.here.sdk.mapview.RenderSize.Unit)"
    class="section detail">

    ### MapMarker3D

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") at,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image,
    double scale, @NonNull
    [RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview") unit)</span>

    </div>

    <div class="block">

    Creates a flat marker from provided map image. Such map marker is a
    flat 3D marker of rectangular shape textured with given image.
    Aspect ratio of the flat marker is determined by aspect ratio of the
    image. Only bitmap images are supported, using a MapImage created
    from SVG data will result in distorted rendering of the flat marker.
    Altitude component of the coordinates, if set, controls 3D marker's
    elevation above ground. If not set, the 3D marker is placed at
    ground level. Size of the rendered flat marker can be specified in
    either world or screen coordinate space. For RenderSize.Unit.PIXELS
    , the flat marker will cover scale \* image's width pixels
    horizontally and scale \* image's height pixels vertically. The size
    of the flat marker remains constant on the screen. For
    RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS the flat marker will
    cover scale \* image's width density independent pixels horizontally
    and scale \* image's height density independent pixels vertically.
    The size of the flat marker remains constant on the screen. For
    RenderSize.Unit.METERS the flat marker will cover scale \* image's
    width meters horizontally and scale \* image's height meters
    vertically. Unlike with pixels or density independent pixels the
    size of the flat marker will grow and shrink together with regular
    map content like streets or buildings.

    </div>

    Parameters:  
    `at` -

    The geographical coordinates where the flat marker is placed
    corresponding to center of the provided map image.

    `image` -

    The MapImage containing the texture data of the flat marker. SVG
    images are not supported.

    `scale` -

    Scale factor applied to the dimensions of the image.

    `unit` -

    Determines whether the size of the flat marker is represented in
    world or in screen space.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double)"
    class="section detail">

    ### MapMarker3D

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") at,
    @NonNull
    [MapMarker3DModel](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel "class in com.here.sdk.mapview") model,
    double scale)</span>

    </div>

    <div class="block">

    Creates an instance of a 3D marker with scale factor. One unit of
    the 3D marker model will cover scale pixels. The size of the 3D
    marker remains constant on the screen. The origin of the 3D model's
    local coordinate system is placed at the specified geographical
    coordinates. Altitude component of the coordinates, if set, controls
    3D marker's elevation above ground. If not set, the 3D marker is
    placed at ground level.

    </div>

    Parameters:  
    `at` -

    The geographical coordinates where the 3D marker is placed
    corresponding to origin of the 3D model's local coordinate system.

    `model` -

    The 3D model used to render the 3D marker.

    `scale` -

    Scale factor to apply to the 3D model.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.RenderSize.Unit)"
    class="section detail">

    ### MapMarker3D

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarker3D</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") at,
    @NonNull
    [MapMarker3DModel](sdk-for-android-explore-com-here-sdk-mapview-mapmarker3dmodel "class in com.here.sdk.mapview") model,
    double scale, @NonNull
    [RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview") unit)</span>

    </div>

    <div class="block">

    Creates a new 3D marker at given world coordinates, using the
    supplied 3D model. The unit specifies how the 3D geometry of the
    model is interpreted (meters for world space, pixels or density
    independent pixels for screen space), while scale determines its
    relative size. For RenderSize.Unit.PIXELS one unit of the 3D marker
    model will cover scale pixels. The size of the 3D marker remains
    constant on the screen. For
    RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS one unit of the 3D marker
    model will cover scale density independent pixels. The size of the
    3D marker remains constant on the screen. For RenderSize.Unit.METERS
    one unit of the 3D marker model will cover scale meters in the real
    world. Unlike with pixels or density-independent pixels the size of
    the 3D marker will grow and shrink together with regular map content
    like streets or buildings. The origin of the 3D model's local
    coordinate system is placed at the specified geographical
    coordinates. Altitude component of the coordinates, if set, controls
    3D marker's elevation above ground. If not set, the 3D marker is
    placed at ground level.

    </div>

    Parameters:  
    `at` -

    The geographical coordinates where the 3D marker is placed
    corresponding to origin of the 3D model's local coordinate system.

    `model` -

    The 3D model used to render the 3D marker.

    `scale` -

    Scale factor to apply to the 3D model.

    `unit` -

    Determines the unit of the model vertices and whether the size of
    the 3D marker is expressed in world or screen space.

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-getCoordinates()"
    class="section detail">

    ### getCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getCoordinates</span>()

    </div>

    <div class="block">

    Gets the 3D marker's position on the map corresponding to the origin
    of the 3D marker model coordinate system. The altitude component of
    the coordinates, if set, controls 3D marker's elevation above
    ground. If not set, the 3D marker is placed at ground level.

    </div>

    Returns:  
    The position of the 3D marker on the map corresponding to the origin
    of the 3D marker model coordinate system.

    </div>
<div id="sdk-for-android-explore-setCoordinates(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### setCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCoordinates</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the 3D marker's position on the map corresponding to the origin
    of the 3D marker model coordinate system. The altitude component of
    the coordinates, if set, controls 3D marker's elevation above
    ground. If not set, the 3D marker is placed at ground level.

    </div>

    Parameters:  
    `value` -

    The position of the 3D marker on the map corresponding to the origin
    of the 3D marker model coordinate system.

    </div>
<div id="sdk-for-android-explore-getMetadata()"
    class="section detail">

    ### getMetadata

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")</span> <span class="element-name">getMetadata</span>()

    </div>

    <div class="block">

    Gets the Metadata instance attached to this 3D marker. The default
    value is null .

    </div>

    Returns:  
    The
    [`Metadata`](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")
    instance attached to this 3D marker.

    </div>
<div id="sdk-for-android-explore-setMetadata(com.here.sdk.core.Metadata)"
    class="section detail">

    ### setMetadata

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><span class="parameters">(@Nullable
    [Metadata](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Sets the Metadata instance attached to this 3D marker.

    </div>

    Parameters:  
    `value` -

    The
    [`Metadata`](sdk-for-android-explore-com-here-sdk-core-metadata "class in com.here.sdk.core")
    instance attached to this 3D marker.

    </div>
<div id="sdk-for-android-explore-getBearing()"
    class="section detail">

    ### getBearing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getBearing</span>()

    </div>

    <div class="block">

    Gets the bearing of the 3D model in degrees. The bearing axis is
    perpendicular to the ground and passes through the 3D marker's
    location. The Z-axis of the model is aligned with bearing axis.

    </div>

    Returns:  
    The bearing of the 3D model in degrees, from the true North in
    clockwise direction.

    </div>
<div id="sdk-for-android-explore-setBearing(double)"
    class="section detail">

    ### setBearing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBearing</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the bearing of the 3D model in degrees. The bearing axis is
    perpendicular to the ground and passes through the 3D marker's
    location. The Z-axis of the model is aligned with bearing axis.

    </div>

    Parameters:  
    `value` -

    The bearing of the 3D model in degrees, from the true North in
    clockwise direction.

    </div>
<div id="sdk-for-android-explore-getRoll()" class="section detail">

    ### getRoll

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getRoll</span>()

    </div>

    <div class="block">

    Gets the roll of the 3D model in degrees. The roll axis is parallel
    to the ground, passes through the 3D marker's location and is
    aligned initially with the true North. However, when the bearing
    changes, it rotates around the bearing axis with the 3D marker.
    Positive/negative values cause a clockwise/counterclockwise rotation
    when viewing along the axis in the direction of the true North. The
    Y-axis of the model is aligned with the roll axis.

    </div>

    Returns:  
    The roll angle of the 3D model in degrees.

    </div>
<div id="sdk-for-android-explore-setRoll(double)"
    class="section detail">

    ### setRoll

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRoll</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the roll of the 3D model in degrees. The roll axis is parallel
    to the ground, passes through the 3D marker's location and is
    aligned initially with the true North. However, when the bearing
    changes, it rotates around the bearing axis with the 3D marker.
    Positive/negative values cause a clockwise/counterclockwise rotation
    when viewing along the axis in the direction of the true North. The
    Y-axis of the model is aligned with the roll axis.

    </div>

    Parameters:  
    `value` -

    The roll angle of the 3D model in degrees.

    </div>
<div id="sdk-for-android-explore-getPitch()" class="section detail">

    ### getPitch

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPitch</span>()

    </div>

    <div class="block">

    Gets the pitch of the 3D model in degrees. The pitch axis is
    parallel to the ground, passes through the location of the 3D marker
    and aligns with the longitude axis if the bearing is 0. However,
    this axis rotates with the 3D marker according to the bearing value.
    Negative values cause the top of the 3D marker to lean forward. The
    X-axis of the model is aligned with pitch axis.

    </div>

    Returns:  
    The pitch of the 3D model in degrees.

    </div>
<div id="sdk-for-android-explore-setPitch(double)"
    class="section detail">

    ### setPitch

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPitch</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the pitch of the 3D model in degrees. The pitch axis is
    parallel to the ground, passes through the location of the 3D marker
    and aligns with the longitude axis if the bearing is 0. However,
    this axis rotates with the 3D marker according to the bearing value.
    Negative values cause the top of the 3D marker to lean forward. The
    X-axis of the model is aligned with pitch axis.

    </div>

    Parameters:  
    `value` -

    The pitch of the 3D model in degrees.

    </div>
<div id="sdk-for-android-explore-getScale()" class="section detail">

    ### getScale

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getScale</span>()

    </div>

    <div class="block">

    Gets the scale factor applied to the 3D model before rendering.

    </div>

    Returns:  
    Scale factor applied to the 3D model before rendering.

    </div>
<div id="sdk-for-android-explore-setScale(double)"
    class="section detail">

    ### setScale

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setScale</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the scale factor, to be applied to the 3D model before
    rendering.

    </div>

    Parameters:  
    `value` -

    Scale factor applied to the 3D model before rendering.

    </div>
<div id="sdk-for-android-explore-isDepthCheckEnabled()"
    class="section detail">

    ### isDepthCheckEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDepthCheckEnabled</span>()

    </div>

    <div class="block">

    Returns true if depth check is enabled. If set to false , the 3D
    marker will always appear in front of any other map objects. If set
    to true the 3D marker might be occluded by other map objects like
    extruded buildings. By default depth check is set to false . Use the
    altitude of the getCoordinates() to position the 3D marker
    sufficiently high above the surface. Setting depth check to true
    will fix visual glitches where components of the marker 3D model
    unexpectedly shine through.

    </div>

    Returns:  
    Determines whether the depth of the 3D marker's vertices is
    considered during rendering.

    </div>
<div id="sdk-for-android-explore-setDepthCheckEnabled(boolean)"
    class="section detail">

    ### setDepthCheckEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDepthCheckEnabled</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Set whether the depth of the 3D marker's vertices is considered
    during rendering. If set to false , the 3D marker will always appear
    in front of any other map objects. If set to true the 3D marker
    might be occluded by other map objects like extruded buildings. By
    default depth check is set to false . Use the altitude of the
    getCoordinates() to position the 3D marker sufficiently high above
    the surface. Setting depth check to true will fix visual glitches
    where components of the marker 3D model unexpectedly shine through.

    </div>

    Parameters:  
    `value` -

    Determines whether the depth of the 3D marker's vertices is
    considered during rendering.

    </div>
<div id="sdk-for-android-explore-isRenderInternalsEnabled()"
    class="section detail">

    ### isRenderInternalsEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRenderInternalsEnabled</span>()

    </div>

    <div class="block">

    Returns a flag indicating whether to render internal geometry of a
    3D marker occluded by its front facing polygons. Default value is
    false . Default value is false . Can be used with translucent 3D
    marker. Note: with this flag enabled for 3D marker with depth check
    enabled, rendering is performed in two passes: first pass with
    front-face, second pass with back-face culling enabled. With this
    flag enabled for 3D marker with depth check disabled rendering is
    performed in a single pass with back-face culling disabled.

    </div>

    Returns:  
    Indicates whether to render internal geometry of a 3D marker
    occluded by its front facing polygons.

    </div>
<div id="sdk-for-android-explore-setRenderInternalsEnabled(boolean)"
    class="section detail">

    ### setRenderInternalsEnabled

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRenderInternalsEnabled</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets a flag indicating whether to render internal geometry of a 3D
    marker occluded by its front facing polygons. Default value is false
    . Can be used with translucent 3D marker. Note: with this flag
    enabled for 3D marker with depth check enabled, rendering is
    performed in two passes: first pass with front-face, second pass
    with back-face culling enabled. With this flag enabled for 3D marker
    with depth check disabled rendering is performed in a single pass
    with back-face culling disabled.

    </div>

    Parameters:  
    `value` -

    Indicates whether to render internal geometry of a 3D marker
    occluded by its front facing polygons.

    </div>
<div id="sdk-for-android-explore-getOpacity()"
    class="section detail">

    ### getOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()

    </div>

    <div class="block">

    Returns an opacity factor which specifies the translucency of a 3D
    map marker. The factor is applied to the alpha channel of the
    resulting texture of the marker. Default value is 1.0 meaning marker
    is displayed with the default opacity of the texture image or the
    specified fill color specified in MapMarker3DModel .

    </div>

    Returns:  
    The opacity factor adjusting the opacity of a 3D marker.

    </div>
<div id="sdk-for-android-explore-setOpacity(double)"
    class="section detail">

    ### setOpacity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets an opacity factor which specifies the translucency of a 3D map
    marker. Provided value is clamped to the \[0.0, 1.0\] range. The
    factor is applied to the alpha channel of the resulting texture of
    the marker. Default value is 1.0 meaning marker is displayed with
    the default opacity of the texture image or the specified fill color
    specified in MapMarker3DModel .

    </div>

    Parameters:  
    `value` -

    The opacity factor adjusting the opacity of a 3D marker.

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

    Gets the list of visibility ranges. A range is half open -
    \[minimumZoomLevel, maximumZoomLevel), the given maximum value is
    not contained in the range. When empty (the default), the 3D marker
    is visible without map measure restrictions. Only MapMeasureRange of
    MapMeasure.Kind.ZOOM_LEVEL type are supported. MapMeasureRange of
    other unsupported types will be ignored.

    </div>

    Returns:  
    The list of visibility ranges. The 3D marker is visible only inside
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

    Sets visibility ranges for this 3D marker. A range is half open -
    \[minimumZoomLevel, maximumZoomLevel), the given maximum value is
    not contained in the range. When empty (the default), the 3D marker
    is visible without map measure restrictions. Only MapMeasureRange of
    MapMeasure.Kind.ZOOM_LEVEL type are supported. MapMeasureRange of
    other unsupported types will be ignored.

    </div>

    Parameters:  
    `value` -

    The list of visibility ranges. The 3D marker is visible only inside
    these map measure ranges.

    </div>

  </div>

</div>

