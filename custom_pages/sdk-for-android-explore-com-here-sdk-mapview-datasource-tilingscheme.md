---
title: "TilingScheme (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< TilingScheme \> com.here.sdk.mapview.datasource.TilingScheme → java.lang.Enum \< TilingScheme \> com.here.sdk.mapview.datasource.TilingScheme → com.here.sdk.mapview.datasource.TilingScheme

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`[`TilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">TilingScheme</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")\></span>

</div>

<div class="block">

List of available data tiling schemes. X axis has the origin at -180 longitude and is increasing in east direction. Y axis has the origin at max latitude and is increasing in south direction. For half quad tree schemes, only the uppper half of the tree is used.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme#HALF_QUAD_TREE_EQUIRECTANGULAR" class="member-name-link"><code>HALF_QUAD_TREE_EQUIRECTANGULAR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme#HALF_QUAD_TREE_IDENTITY" class="member-name-link"><code>HALF_QUAD_TREE_IDENTITY</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme#HALF_QUAD_TREE_MERCATOR" class="member-name-link"><code>HALF_QUAD_TREE_MERCATOR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme#QUAD_TREE_EQUIRECTANGULAR" class="member-name-link"><code>QUAD_TREE_EQUIRECTANGULAR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A tiling scheme that splits each level tile into 4 equal-sized subtiles.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme#QUAD_TREE_IDENTITY" class="member-name-link"><code>QUAD_TREE_IDENTITY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A tiling scheme that splits each level tile into 4 equal-sized subtiles.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme#QUAD_TREE_MERCATOR" class="member-name-link"><code>QUAD_TREE_MERCATOR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A tiling scheme that splits each level tile into 4 equal-sized subtiles.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`TilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`TilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-HALF_QUAD_TREE_IDENTITY" class="section detail">

    ### HALF_QUAD_TREE_IDENTITY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">HALF_QUAD_TREE_IDENTITY</span>

    </div>

    <div class="block">

    A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

    </div>

    </div>

  - <div id="sdk-for-android-explore-HALF_QUAD_TREE_MERCATOR" class="section detail">

    ### HALF_QUAD_TREE_MERCATOR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">HALF_QUAD_TREE_MERCATOR</span>

    </div>

    <div class="block">

    A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the web-mercator projection.

    </div>

    </div>

  - <div id="sdk-for-android-explore-HALF_QUAD_TREE_EQUIRECTANGULAR" class="section detail">

    ### HALF_QUAD_TREE_EQUIRECTANGULAR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">HALF_QUAD_TREE_EQUIRECTANGULAR</span>

    </div>

    <div class="block">

    A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.

    </div>

    </div>

  - <div id="sdk-for-android-explore-QUAD_TREE_IDENTITY" class="section detail">

    ### QUAD_TREE_IDENTITY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">QUAD_TREE_IDENTITY</span>

    </div>

    <div class="block">

    A tiling scheme that splits each level tile into 4 equal-sized subtiles.

    </div>

    </div>

  - <div id="sdk-for-android-explore-QUAD_TREE_MERCATOR" class="section detail">

    ### QUAD_TREE_MERCATOR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">QUAD_TREE_MERCATOR</span>

    </div>

    <div class="block">

    A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the web-mercator projection.

    </div>

    </div>

  - <div id="sdk-for-android-explore-QUAD_TREE_EQUIRECTANGULAR" class="section detail">

    ### QUAD_TREE_EQUIRECTANGULAR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">QUAD_TREE_EQUIRECTANGULAR</span>

    </div>

    <div class="block">

    A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

