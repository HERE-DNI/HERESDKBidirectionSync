---
title: "MapPolyline.SolidRepresentation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidrepresentation"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase
com.here.sdk.mapview.MapItemRepresentation
com.here.sdk.mapview.MapPolyline.Representation
com.here.sdk.mapview.MapPolyline.SolidRepresentation →
com.here.NativeBase com.here.sdk.mapview.MapItemRepresentation
com.here.sdk.mapview.MapPolyline.Representation
com.here.sdk.mapview.MapPolyline.SolidRepresentation →
com.here.sdk.mapview.MapItemRepresentation
com.here.sdk.mapview.MapPolyline.Representation
com.here.sdk.mapview.MapPolyline.SolidRepresentation →
com.here.sdk.mapview.MapPolyline.Representation
com.here.sdk.mapview.MapPolyline.SolidRepresentation →
com.here.sdk.mapview.MapPolyline.SolidRepresentation

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapPolyline.SolidRepresentation</span>
<span class="extends-implements">extends
[MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview")</span>

</div>

<div class="block">

Representation for a solid line without outline. Can represent polylines
that have constant width or width dependent on the map zoom. To achieve
constant width lines, use MapMeasureDependentRenderSize with a single
value. To achieve line width dependent on map zoom, use
MapMeasureDependentRenderSize with multiple values. For MapMeasure.Kind
only MapMeasure.Kind.ZOOM_LEVEL is supported. For RenderSize.Unit only
RenderSize.Unit.PIXELS is supported.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class com.here.sdk.mapview.[MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview")

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

      SolidRepresentation ( MapMeasureDependentRenderSize lineWidth, Color color, LineCap capShape)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a representation for a solid line without outline.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SolidRepresentation ( MapMeasureDependentRenderSize lineWidth, Color color, MapMeasureDependentRenderSize outlineWidth, Color outlineColor, LineCap capShape)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a representation for a solid line with outline.

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

  [`LineCap`](sdk-for-android-explore-com-here-sdk-mapview-linecap "enum class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCapShape ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the cap shape of the polyline and its outline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLineColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the color of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLineWidth ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent polyline width.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOutlineColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the color of outline of the polyline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOutlineWidth ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent polyline outline width.

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

  - <div id="sdk-for-android-explore-init-com-here-sdk-mapview-MapMeasureDependentRenderSize-com-here-sdk-core-Color-com-here-sdk-mapview-LineCap"
    class="section detail">

    ### SolidRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SolidRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color,
    @NonNull
    [LineCap](sdk-for-android-explore-com-here-sdk-mapview-linecap "enum class in com.here.sdk.mapview") capShape)</span>
    throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a representation for a solid line without outline. At map
    measures smaller than smallest map measure in the lineWidth line
    width is constant and equal to the width given for the smallest map
    measure in the lineWidth . At map measures bigger than biggest map
    measure in the lineWidth line width is constant and equal to the
    width given for the biggest map measure in the lineWidth . At map
    measures between two nearest given map measures line width is
    linearly interpolated between width values given for these map
    measures. For MapMeasure.Kind only MapMeasure.Kind.ZOOM_LEVEL is
    supported. For RenderSize.Unit only RenderSize.Unit.PIXELS is
    supported. lineWidth must not be 0 ( lineWidth.sizes with all values
    set to 0.0).

    </div>

    Parameters:  
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `color` -

    The color of the polyline.

    `capShape` -

    The cap shape applied to both ends of the polyline.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-mapview-MapMeasureDependentRenderSize-com-here-sdk-core-Color-com-here-sdk-mapview-MapMeasureDependentRenderSize-com-here-sdk-core-Color-com-here-sdk-mapview-LineCap"
    class="section detail">

    ### SolidRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SolidRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") outlineWidth,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") outlineColor,
    @NonNull
    [LineCap](sdk-for-android-explore-com-here-sdk-mapview-linecap "enum class in com.here.sdk.mapview") capShape)</span>
    throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a representation for a solid line with outline. The total
    width of the polyline is line width + 2 \* outline width . At map
    measures smaller than smallest map measure in the lineWidth and
    outlineWidth , the value is constant and equal to the width given
    for the smallest map measure in the lineWidth and outlineWidth . At
    map measures bigger than biggest map measure in the lineWidth and
    outlineWidth , the value is constant and equal to the width given
    for the biggest map measure in the lineWidth and outlineWidth . At
    map measures between two nearest given map measure is linearly
    interpolated between width values given for these map measures. For
    MapMeasure.Kind only MapMeasure.Kind.ZOOM_LEVEL is supported. For
    RenderSize.Unit only RenderSize.Unit.PIXELS is supported. lineWidth
    must not be 0 ( lineWidth.sizes with all values set to 0.0).

    </div>

    Parameters:  
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `color` -

    The color of the polyline.

    `outlineWidth` -

    The width of the outline on one side of the polyline depending on
    the map measure.

    `outlineColor` -

    The outline color of the polyline.

    `capShape` -

    The cap shape applied to both ends of the polyline.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getLineWidth"
    class="section detail">

    ### getLineWidth

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getLineWidth</span>()

    </div>

    <div class="block">

    Gets the map measure dependent polyline width. At map measures
    smaller than smallest map measure in the lineWidth line width is
    constant and equal to the width given for the smallest map measure
    in the lineWidth . At map measures bigger than biggest map measure
    in the lineWidth line width is constant and equal to the width given
    for the biggest map measure in the lineWidth . At map measures
    between two nearest given map measures, the values are linearly
    interpolated between values given for these map measures.

    </div>

    Returns:  
    The width of the polyline depending on the map measure.

    </div>

  - <div id="sdk-for-android-explore-getLineColor"
    class="section detail">

    ### getLineColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getLineColor</span>()

    </div>

    <div class="block">

    Gets the color of the polyline.

    </div>

    Returns:  
    The color of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getOutlineWidth"
    class="section detail">

    ### getOutlineWidth

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getOutlineWidth</span>()

    </div>

    <div class="block">

    Gets the map measure dependent polyline outline width. The total
    width of the polyline is line width + 2 \* outline width . At map
    measures smaller than smallest map measure in the outlineWidth ,
    outline width is constant and equal to the width given for the
    smallest map measure in the outlineWidth . At map measures bigger
    than biggest map measure in the outlineWidth , outline width is
    constant and equal to the width given for the biggest map measure in
    the outlineWidth . At map measures between two nearest given map
    measures, the values are linearly interpolated between values given
    for these map measures.

    </div>

    Returns:  
    The width of the outline on one side of the polyline depending on
    the map measure.

    </div>

  - <div id="sdk-for-android-explore-getOutlineColor"
    class="section detail">

    ### getOutlineColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getOutlineColor</span>()

    </div>

    <div class="block">

    Gets the color of outline of the polyline.

    </div>

    Returns:  
    The outline color of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getCapShape"
    class="section detail">

    ### getCapShape

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LineCap](sdk-for-android-explore-com-here-sdk-mapview-linecap "enum class in com.here.sdk.mapview")</span> <span class="element-name">getCapShape</span>()

    </div>

    <div class="block">

    Returns the cap shape of the polyline and its outline.

    </div>

    Returns:  
    The cap shape applied to both ends of the polyline and its outline.

    </div>

  </div>

