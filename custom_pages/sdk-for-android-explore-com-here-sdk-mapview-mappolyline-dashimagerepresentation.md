---
title: "MapPolyline.DashImageRepresentation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashimagerepresentation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapItemRepresentationcom.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.DashImageRepresentation
→ com.here.NativeBase →
com.here.sdk.mapview.MapItemRepresentationcom.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.DashImageRepresentation
→ com.here.sdk.mapview.MapItemRepresentation →
com.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.DashImageRepresentation
→ com.here.sdk.mapview.MapPolyline.Representation →
com.here.sdk.mapview.MapPolyline.DashImageRepresentation

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapPolyline.DashImageRepresentation</span>
<span class="extends-implements">extends
[MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview")</span>

</div>

<div class="block">

Represents a dash pattern for the map polyline consisting of images
rendered with certain gaps from each other. This dash pattern
representation consists only of images rendered at certain points along
the polyline. For rendering them without any distortions, polyline gets
sliced into series of straight segments that are multiple of sum of dash
and gap lengths. For this reason, the new polyline geometry might not
align fully with original geometry. The getDashImage() is stretched
according to getDashLength() and getDashWidth() , with image's width
matched to dashLength and image's height matched to dashWidth . The
image is oriented so that its bottom is on the left-hand side between
vertices n and n+1 . The spacing between images is specified by
getGapLength() . Note: This is a beta release of this feature, so there
could be a few bugs and unexpected behaviors. Related APIs may change
for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  [`MapPolyline.Representation.InstantiationErrorCode`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview"), [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

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

      DashImageRepresentation(MapMeasureDependentRenderSize dashLength,
       MapMeasureDependentRenderSize dashWidth,
       MapImage image)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a uniform dash pattern in which the length of a gap is the
  same as the length of a dash.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      DashImageRepresentation(MapMeasureDependentRenderSize dashLength,
       MapMeasureDependentRenderSize gapLength,
       MapMeasureDependentRenderSize dashWidth,
       MapImage image)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a simple dash pattern in which the lengths of a dash and gap
  can be different.

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

  [`MapImage`](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDashImage()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the image that is rendered in place of dash space.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDashLength()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent length of a dash, to which image width
  is stretched.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDashWidth()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent width of a dash, to which image height
  is stretched.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGapLength()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent length of a gap between dash images.

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

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### DashImageRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DashImageRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") dashWidth,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image)</span>
    throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a uniform dash pattern in which the length of a gap is the
    same as the length of a dash. Dashes are rendered as image. This
    allows for patterns like ' — — — —' or ' —— —— ——' . For
    MapMeasureDependentRenderSize supplied for dashLength and dashWidth
    , only MapMeasure.Kind.ZOOM_LEVEL is supported for
    MapMeasureDependentRenderSize.measureKind and only
    RenderSize.Unit.METERS is supported for
    MapMeasureDependentRenderSize.sizeUnit . Only map measure values in
    range \[3-19\] are supported. The value of the keys in
    MapMeasureDependentRenderSize.sizes is truncated to integer values,
    hence only a single value can be provided per zoom level. The values
    are interpolated linearly between zoom levels.

    </div>

    Parameters:  
    `dashLength` -

    The map measure dependent length of a dash, to which image width is
    stretched.

    `dashWidth` -

    The map measure dependent width of a dash, to which image height is
    stretched.

    `image` -

    Image to be rendered in place of dash space. It is stretched to
    match `dashWidth` and `dashLength`.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)"
    class="section detail">

    ### DashImageRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DashImageRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") gapLength,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") dashWidth,
    @NonNull
    [MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview") image)</span>
    throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a simple dash pattern in which the lengths of a dash and gap
    can be different. Dashes are rendered as image. This allows for
    patterns like ' — — — —' or ' ——— ——— ———' . For
    MapMeasureDependentRenderSize supplied for dashLength , gapLength
    and dashWidth , only MapMeasure.Kind.ZOOM_LEVEL is supported for
    MapMeasureDependentRenderSize.measureKind and only
    RenderSize.Unit.METERS is supported for
    MapMeasureDependentRenderSize.sizeUnit . Only map measure values in
    range \[3-19\] are supported. The value of the keys in
    MapMeasureDependentRenderSize.sizes is truncated to integer values,
    hence only a single value can be provided per zoom level. The values
    are interpolated linearly between zoom levels.

    </div>

    Parameters:  
    `dashLength` -

    The map measure dependent length of a dash, to which image width is
    stretched.

    `gapLength` -

    The map measure dependent length of a gap between dash images.

    `dashWidth` -

    The map measure dependent width of a dash, to which image height is
    stretched.

    `image` -

    Image to be rendered in place of dash space. It is stretched to
    match `dashWidth` and `dashLength`.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getDashImage()"
    class="section detail">

    ### getDashImage

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">getDashImage</span>()

    </div>

    <div class="block">

    Gets the image that is rendered in place of dash space. It is
    stretched to fill whole polyline width and length of each dash.

    </div>

    Returns:  
    Image to be rendered in place of dash space.

    </div>

  - <div id="sdk-for-android-explore-getDashLength()"
    class="section detail">

    ### getDashLength

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getDashLength</span>()

    </div>

    <div class="block">

    Gets the map measure dependent length of a dash, to which image
    width is stretched.

    </div>

    Returns:  
    The map measure dependent length of a dash, to which image width is
    stretched.

    </div>

  - <div id="sdk-for-android-explore-getGapLength()"
    class="section detail">

    ### getGapLength

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getGapLength</span>()

    </div>

    <div class="block">

    Gets the map measure dependent length of a gap between dash images.

    </div>

    Returns:  
    The map measure dependent length of a gap between dash images.

    </div>

  - <div id="sdk-for-android-explore-getDashWidth()"
    class="section detail">

    ### getDashWidth

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getDashWidth</span>()

    </div>

    <div class="block">

    Gets the map measure dependent width of a dash, to which image
    height is stretched.

    </div>

    Returns:  
    The map measure dependent width of a dash, to which image height is
    stretched.

    </div>

  </div>

</div>

