---
title: "MapMarker.TextStyle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapMarker.TextStyle →
com.here.NativeBase → com.here.sdk.mapview.MapMarker.TextStyle

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapMarker](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapMarker.TextStyle</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Styling options for the text of a MapMarker .

</div>

</div>

<div class="section summary">

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

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapMarker.TextStyle.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to create a MapMarker.TextStyle .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMarker.TextStyle.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create a
  MapMarker.TextStyle instance.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-placement"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapMarker.TextStyle.Placement</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Represents text placement with respect to the icon of a MapMarker .

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

      TextStyle()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a default set of styling options for the text of a MapMarker
  that consists of the following values: Text size: 18 pixels Text
  color: opaque white Text outline size: 0 pixels Text outline color:
  opaque black Text placement: MapMarker.TextStyle.Placement.BOTTOM

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      TextStyle(double textSize,
       Color textColor,
       double textOutlineSize,
       Color textOutlineColor,
       List<MapMarker.TextStyle.Placement> placements)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a set of styling options for the text of a MapMarker .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      TextStyle(double textSize,
       Color textColor,
       double textOutlineSize,
       Color textOutlineColor,
       List<MapMarker.TextStyle.Placement> placements,
       String fontName)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a set of styling options for the text of a MapMarker .

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

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFontName()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the font name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapMarker.TextStyle.Placement`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-placement "enum class in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPlacements()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the possible text placements relative to the icon of a MapMarker
  .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTextColor()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the text color.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTextOutlineColor()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the text outline color.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTextOutlineSize()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the text outline size in pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTextSize()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the text size in pixels.

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

  - <div id="sdk-for-android-explore-<init>()" class="section detail">

    ### TextStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TextStyle</span>()

    </div>

    <div class="block">

    Creates a default set of styling options for the text of a MapMarker
    that consists of the following values: Text size: 18 pixels Text
    color: opaque white Text outline size: 0 pixels Text outline color:
    opaque black Text placement: MapMarker.TextStyle.Placement.BOTTOM
    Once the resulting TextStyle is applied to a MapMarker , its text
    will be centered over its image. The font will be 18 pixels wide,
    colored opaque white and will have no visible outline.

    </div>

    </div>

  - <div id="sdk-for-android-explore-<init>(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List)"
    class="section detail">

    ### TextStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TextStyle</span><span class="parameters">(double textSize,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") textColor,
    double textOutlineSize, @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") textOutlineColor,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\> placements)</span>
    throws
    <span class="exceptions">[MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a set of styling options for the text of a MapMarker . List
    of placements is used to specify allowed placement of text relative
    to the icon. When marker overlapping is allowed as set by
    MapMarker.setOverlapAllowed(boolean) , only first placement element
    is considered. Otherwise the placement value is chosen so that the
    text does not overlap with other MapMarker instances. Placement
    values are prioritized according to the order in which they appear
    in the list. Lists with duplicate entries as well as empty lists are
    not supported.

    </div>

    Parameters:  
    `textSize` -

    The size of the text in pixels. Only positive values are supported.

    `textColor` -

    The text color.

    `textOutlineSize` -

    The size of the text outline in pixels. Only non-negative values are
    supported.

    `textOutlineColor` -

    The color of the text outline.

    `placements` -

    List of allowed placements of the text relative to the icon of a
    [`MapMarker`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview").

    Throws:  
    [`MapMarker.TextStyle.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  - <div id="sdk-for-android-explore-<init>(double,com.here.sdk.core.Color,double,com.here.sdk.core.Color,java.util.List,java.lang.String)"
    class="section detail">

    ### TextStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TextStyle</span><span class="parameters">(double textSize,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") textColor,
    double textOutlineSize, @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") textOutlineColor,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\> placements,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> fontName)</span>
    throws
    <span class="exceptions">[MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a set of styling options for the text of a MapMarker . Note:
    This is a beta release of this feature, so there could be a few bugs
    and unexpected behavior. Related APIs may change for new releases
    without a deprecation process. List of placements is used to specify
    allowed placement of text relative to the icon. When marker
    overlapping is allowed as set by
    MapMarker.setOverlapAllowed(boolean) , only first placement element
    is considered. Otherwise the placement value is chosen so that the
    text does not overlap with other MapMarker instances. Placement
    values are prioritized according to the order in which they appear
    in the list. Lists with duplicate entries as well as empty lists are
    not supported.

    </div>

    Parameters:  
    `textSize` -

    The size of the text in pixels. Only positive values are supported.

    `textColor` -

    The text color.

    `textOutlineSize` -

    The size of the text outline in pixels. Only non-negative values are
    supported.

    `textOutlineColor` -

    The color of the text outline.

    `placements` -

    List of allowed placements of the text relative to the icon of a
    [`MapMarker`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview").

    `fontName` -

    Font name, registered with `AssetsManager.registerFont`. If empty
    string is provided, a default font will be used.

    Throws:  
    [`MapMarker.TextStyle.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getFontName()"
    class="section detail">

    ### getFontName

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getFontName</span>()

    </div>

    <div class="block">

    Gets the font name.

    </div>

    Returns:  
    The font used in the text style.

    </div>

  - <div id="sdk-for-android-explore-getTextSize()"
    class="section detail">

    ### getTextSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getTextSize</span>()

    </div>

    <div class="block">

    Gets the text size in pixels.

    </div>

    Returns:  
    The text size in pixels.

    </div>

  - <div id="sdk-for-android-explore-getTextColor()"
    class="section detail">

    ### getTextColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getTextColor</span>()

    </div>

    <div class="block">

    Gets the text color.

    </div>

    Returns:  
    The text color.

    </div>

  - <div id="sdk-for-android-explore-getTextOutlineSize()"
    class="section detail">

    ### getTextOutlineSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getTextOutlineSize</span>()

    </div>

    <div class="block">

    Gets the text outline size in pixels.

    </div>

    Returns:  
    The text outline size in pixels.

    </div>

  - <div id="sdk-for-android-explore-getTextOutlineColor()"
    class="section detail">

    ### getTextOutlineColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getTextOutlineColor</span>()

    </div>

    <div class="block">

    Gets the text outline color.

    </div>

    Returns:  
    The text outline color.

    </div>

  - <div id="sdk-for-android-explore-getPlacements()"
    class="section detail">

    ### getPlacements

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapMarker.TextStyle.Placement](sdk-for-android-explore-com-here-sdk-mapview-mapmarker-textstyle-placement "enum class in com.here.sdk.mapview")\></span> <span class="element-name">getPlacements</span>()

    </div>

    <div class="block">

    Gets the possible text placements relative to the icon of a
    MapMarker .

    </div>

    Returns:  
    List of possible text placements relative to the icon of a
    [`MapMarker`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview").

    </div>

  </div>

</div>

