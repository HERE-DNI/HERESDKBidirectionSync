---
title: "RasterDataSourceConfiguration.Provider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider → com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
[RasterDataSourceConfiguration](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">RasterDataSourceConfiguration.Provider</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Configuration of a data provider.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#hasAlphaChannel" class="member-name-link"><code>hasAlphaChannel</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A flag indicating whether the image content contains an alpha channel for transparency.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#headers" class="member-name-link"><code>headers</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The optional name-value pairs specifying HTTP headers that are passed with each tile request.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#storageLevels" class="member-name-link"><code>storageLevels</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The storage levels available for this data source.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`TilingScheme`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#tilingScheme" class="member-name-link"><code>tilingScheme</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The tiling scheme used by this source.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`TileUrlProviderCallback`](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#urlProvider" class="member-name-link"><code>urlProvider</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Provides a function that generates URLs based on tile coordinates and storage level.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      Provider ( TileUrlProviderCallback urlProvider, TilingScheme tilingScheme, List < Integer > storageLevels)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Provider ( TileUrlProviderCallback urlProvider, TilingScheme tilingScheme, List < Integer > storageLevels,
       boolean hasAlphaChannel, Map < String , String > headers)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-urlProvider" class="section detail">

    ### urlProvider

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TileUrlProviderCallback](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource")</span> <span class="element-name">urlProvider</span>

    </div>

    <div class="block">

    Provides a function that generates URLs based on tile coordinates and storage level.

    </div>

    </div>

  - <div id="sdk-for-android-explore-tilingScheme" class="section detail">

    ### tilingScheme

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">tilingScheme</span>

    </div>

    <div class="block">

    The tiling scheme used by this source.

    </div>

    </div>

  - <div id="sdk-for-android-explore-storageLevels" class="section detail">

    ### storageLevels

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\></span> <span class="element-name">storageLevels</span>

    </div>

    <div class="block">

    The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

    </div>

    </div>

  - <div id="sdk-for-android-explore-hasAlphaChannel" class="section detail">

    ### hasAlphaChannel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAlphaChannel</span>

    </div>

    <div class="block">

    A flag indicating whether the image content contains an alpha channel for transparency. Default value is false .

    </div>

    </div>

  - <div id="sdk-for-android-explore-headers" class="section detail">

    ### headers

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\></span> <span class="element-name">headers</span>

    </div>

    <div class="block">

    The optional name-value pairs specifying HTTP headers that are passed with each tile request.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-mapview-datasource-TileUrlProviderCallback-com-here-sdk-mapview-datasource-TilingScheme-java-util-List-boolean-java-util-Map" class="section detail">

    ### Provider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Provider</span><wbr></wbr><span class="parameters">(@NonNull [TileUrlProviderCallback](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider, @NonNull [TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\> storageLevels, boolean hasAlphaChannel, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\> headers)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `urlProvider` -

    Provides a function that generates URLs based on tile coordinates and storage level.

    `tilingScheme` -

    The tiling scheme used by this source.

    `storageLevels` -

    The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

    `hasAlphaChannel` -

    A flag indicating whether the image content contains an alpha channel for transparency. Default value is `false`.

    `headers` -

    The optional name-value pairs specifying HTTP headers that are passed with each tile request.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-mapview-datasource-TileUrlProviderCallback-com-here-sdk-mapview-datasource-TilingScheme-java-util-List" class="section detail">

    ### Provider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Provider</span><wbr></wbr><span class="parameters">(@NonNull [TileUrlProviderCallback](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider, @NonNull [TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>\> storageLevels)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `urlProvider` -

    Provides a function that generates URLs based on tile coordinates and storage level.

    `tilingScheme` -

    The tiling scheme used by this source.

    `storageLevels` -

    The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

