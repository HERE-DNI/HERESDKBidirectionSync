---
title: "MapPolyline.SolidMultiColorRepresentation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapItemRepresentationcom.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.SolidMultiColorRepresentation
→ com.here.NativeBase →
com.here.sdk.mapview.MapItemRepresentationcom.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.SolidMultiColorRepresentation
→ com.here.sdk.mapview.MapItemRepresentation →
com.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.SolidMultiColorRepresentation
→ com.here.sdk.mapview.MapPolyline.Representation →
com.here.sdk.mapview.MapPolyline.SolidMultiColorRepresentation

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapPolyline.SolidMultiColorRepresentation</span>
<span class="extends-implements">extends
[MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview")</span>

</div>

<div class="block">

Representation allows map polyline to be colored in multiple specified
color segments. Color segment is defined by color stops. Color stop is
specified as a polyline length ratio (0.0 - start of the polyline, 1.0 -
end of the polyline). Color stop represents a color change starting at
that exact point up until either the next color stop (if one exists) or
the end of the polyline. Progress color MapPolyline.progressColor
overrides any of the multiple color. Examples: The following
configuration will color map polyline as follows: - from the start to
the middle of it at the 0.5 point - in Red - from the middle point 0.5
to the 0.7 point - in Green - from 0.7 to 1.0 - in Red 'colorStops:
{0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}' Note:
This is a beta release of this feature, so there could be a few bugs and
unexpected behavior. Related APIs may change for new releases without a
deprecation process.

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

      SolidMultiColorRepresentation(MapMeasureDependentRenderSize lineWidth,
       LineCap capShape,
       List<Double> colorStops,
       List<Long> colorIndices,
       List<Color> colors,
       double gradientLength)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a representation for a multicolored line without an outline.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SolidMultiColorRepresentation(MapMeasureDependentRenderSize lineWidth,
       MapMeasureDependentRenderSize outlineWidth,
       Color outlineColor,
       LineCap capShape,
       List<Double> colorStops,
       List<Long> colorIndices,
       List<Color> colors,
       double gradientLength)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a representation for a multicolored line with an outline.

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMultiColorGradientLength(double length)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the multiple color segment gradient length.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMultiColors(List<Double> colorStops,
       List<Long> colorIndices,
       List<Color> colors)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets lists of colors and multiple color segment stops for the polyline
  to be colored in.

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

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)"
    class="section detail">

    ### SolidMultiColorRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SolidMultiColorRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth,
    @NonNull
    [LineCap](sdk-for-android-explore-com-here-sdk-mapview-linecap "enum class in com.here.sdk.mapview") capShape,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> colorStops,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a>\> colorIndices,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")\> colors,
    double gradientLength)</span> throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a representation for a multicolored line without an outline.
    Color segment is defined by color stops. Color stop is specified as
    a polyline length ratio (0.0 - start of the polyline, 1.0 - end of
    the polyline). Color stop represents a color change starting at that
    exact point up until either the next color stop (if one exists) or
    the end of the polyline. Progress color MapPolyline.progressColor
    overrides any of the multiple color. At map measures smaller than
    smallest map measure in the lineWidth line width is constant and
    equal to the width given for the smallest map measure in the
    lineWidth . At map measures bigger than biggest map measure in the
    lineWidth line width is constant and equal to the width given for
    the biggest map measure in the lineWidth . At map measures between
    two nearest given map measures line width is linearly interpolated
    between width values given for these map measures. For
    MapMeasure.Kind only MapMeasure.Kind.ZOOM_LEVEL is supported. For
    RenderSize.Unit only RenderSize.Unit.PIXELS is supported. lineWidth
    must not be 0 ( lineWidth.sizes with all values set to 0.0). Note:
    This is a beta release of this feature, so there could be a few bugs
    and unexpected behavior. Related APIs may change for new releases
    without a deprecation process.

    </div>

    Parameters:  
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `capShape` -

    The cap shape applied to both ends of the polyline.

    `colorStops` -

    List containing color stop values indicating a change of color on a
    polyline. Color stops must be in the range of \[0.0, 1.0\]. Color
    stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3,
    1.0). Duplicate values are not allowed. Color stop list must be of
    the same size as color indices list. Maximum size is 100 color
    stops. An empty list is not allowed. The first color stop value in
    the list must be 0.0.

    `colorIndices` -

    List of color indices (from the color list) corresponding to the
    color stops. Value range is: \[0, (color list size - 1)\]. Values
    outside of the range are not allowed. Color indices list must be of
    the same size as color stop list. Maximum size is 100 color indices.

    `colors` -

    List of colors. Maximum size is 16 colors. An empty list is not
    allowed.

    `gradientLength` -

    Multiple color segment gradient length. Colors of two adjacent color
    segments can be blended to have a nicer visual appeal. Blending
    produces color gradient of specific length which is part of the
    color segment being blended. Start of the segment is blended with a
    color from the previous segment. Blending length is specified as a
    ratio of the smallest color segment length (from the list of color
    stops). E.g. a value of '0.1' means 10% of the length of the
    smallest segment will be blended with a color from its previous
    segment. For this smallest segment gradient length is applied as-is,
    for all other segments it is scaled proportionally based on the
    smallest segment's size to other segment size ratio. Length of '0.0'
    is the default value which means blending will not be applied. Valid
    value range is \[0.0, 1.0\]. Out of range values are not supported.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)"
    class="section detail">

    ### SolidMultiColorRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SolidMultiColorRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") outlineWidth,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") outlineColor,
    @NonNull
    [LineCap](sdk-for-android-explore-com-here-sdk-mapview-linecap "enum class in com.here.sdk.mapview") capShape,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> colorStops,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a>\> colorIndices,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")\> colors,
    double gradientLength)</span> throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a representation for a multicolored line with an outline.
    Color segment is defined by color stops. Color stop is specified as
    a polyline length ratio (0.0 - start of the polyline, 1.0 - end of
    the polyline). Color stop represents a color change starting at that
    exact point up until either the next color stop (if one exists) or
    the end of the polyline. Progress color MapPolyline.progressColor
    overrides any of the multiple color. The total width of the polyline
    is line width + 2 \* outline width . At map measures smaller than
    smallest map measure in the lineWidth and outlineWidth , the value
    is constant and equal to the width given for the smallest map
    measure in the lineWidth and outlineWidth . At map measures bigger
    than biggest map measure in the lineWidth and outlineWidth , the
    value is constant and equal to the width given for the biggest map
    measure in the lineWidth and outlineWidth . At map measures between
    two nearest given map measure is linearly interpolated between width
    values given for these map measures. For MapMeasure.Kind only
    MapMeasure.Kind.ZOOM_LEVEL is supported. For RenderSize.Unit only
    RenderSize.Unit.PIXELS is supported. lineWidth must not be 0 (
    lineWidth.sizes with all values set to 0.0). Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behavior. Related APIs may change for new releases without a
    deprecation process.

    </div>

    Parameters:  
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `outlineWidth` -

    The width of the outline on one side of the polyline depending on
    the map measure.

    `outlineColor` -

    The outline color of the polyline.

    `capShape` -

    The cap shape applied to both ends of the polyline.

    `colorStops` -

    List containing color stop values indicating a change of color on a
    polyline. Color stops must be in the range of \[0.0, 1.0\]. Color
    stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3,
    1.0). Duplicate values are not allowed. Color stop list must be of
    the same size as color indices list. Maximum size is 100 color
    stops. An empty list is not allowed. The first color stop value in
    the list must be 0.0.

    `colorIndices` -

    List of color indices (from the color list) corresponding to the
    color stops. Value range is: \[0, (color list size - 1)\]. Values
    outside of the range are not allowed. Color indices list must be of
    the same size as color stop list. Maximum size is 100 color indices.

    `colors` -

    List of colors. Maximum size is 16 colors. An empty list is not
    allowed.

    `gradientLength` -

    Multiple color segment gradient length. Colors of two adjacent color
    segments can be blended to have a nicer visual appeal. Blending
    produces color gradient of specific length which is part of the
    color segment being blended. Start of the segment is blended with a
    color from the previous segment. Blending length is specified as a
    ratio of the smallest color segment length (from the list of color
    stops). E.g. a value of '0.1' means 10% of the length of the
    smallest segment will be blended with a color from its previous
    segment. For this smallest segment gradient length is applied as-is,
    for all other segments it is scaled proportionally based on the
    smallest segment's size to other segment size ratio. Length of '0.0'
    is the default value which means blending will not be applied. Valid
    value range is \[0.0, 1.0\]. Out of range values are not supported.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-setMultiColors(java.util.List,java.util.List,java.util.List)"
    class="section detail">

    ### setMultiColors

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setMultiColors</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>\> colorStops,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a>\> colorIndices,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")\> colors)</span>

    </div>

    <div class="block">

    Sets lists of colors and multiple color segment stops for the
    polyline to be colored in. When this representation is already set
    on any MapPolyline , values will be applied on that MapPolyline
    right away. If this representation is not set on any MapPolyline ,
    values will be applied once representation is set on a MapPolyline .
    Note: This is a beta release of this feature, so there could be a
    few bugs and unexpected behavior. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `colorStops` -

    List containing color stop values indicating a change of color on a
    polyline. Color stops must be in the range of \[0.0, 1.0\]. Color
    stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3,
    1.0). Duplicate values are not allowed. Color stop list must be of
    the same size as color indices list. Maximum size is 100 color
    stops. An empty list is not allowed. The first color stop value in
    the list must be 0.0.

    `colorIndices` -

    List of color indices (from the color list) corresponding to the
    color stops. Value range is: \[0, (color list size - 1)\]. Values
    outside of the range are not allowed. Color indices list must be of
    the same size as color stop list. Maximum size is 100 color indices.

    `colors` -

    List of colors. Maximum size is 16 colors. An empty list is not
    allowed.

    Returns:  
    Value indicating whether parameters are valid and can be applied.

    </div>

  - <div id="sdk-for-android-explore-setMultiColorGradientLength(double)"
    class="section detail">

    ### setMultiColorGradientLength

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setMultiColorGradientLength</span><span class="parameters">(double length)</span>

    </div>

    <div class="block">

    Sets the multiple color segment gradient length. Colors of two
    adjacent color segments can be blended to have a nicer visual
    appeal. Blending produces color gradient of specific length which is
    part of the color segment being blended. Start of the segment is
    blended with a color from the previous segment. Blending length is
    specified as a ratio of the smallest color segment length (from the
    list of color stops). E.g. a value of '0.1' means 10% of the length
    of the smallest segment will be blended with a color from its
    previous segment. For this smallest segment gradient length is
    applied as-is, for all other segments it is scaled proportionally
    based on the smallest segment's size to other segment size ratio.
    Length of '0.0' is the default value which means blending will not
    be applied. Valid value range is \[0.0, 1.0\]. Out of range values
    are not supported. When this representation is already set on any
    MapPolyline , value will be applied on that MapPolyline right away.
    If this representation is not set on any MapPolyline , value will be
    applied once representation is set on a MapPolyline . Note: This is
    a beta release of this feature, so there could be a few bugs and
    unexpected behavior. Related APIs may change for new releases
    without a deprecation process.

    </div>

    Parameters:  
    `length` -

    Multiple color segment gradient length. Length of '0.0' is the
    default value which means blending will not be applied. Valid value
    range is \[0.0, 1.0\]. Out of range values are not supported.

    Returns:  
    Value indicating whether specified value is valid and can be
    applied.

    </div>

  </div>

</div>

