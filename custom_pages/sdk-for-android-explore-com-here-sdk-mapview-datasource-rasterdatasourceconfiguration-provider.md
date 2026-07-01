---
title: "RasterDataSourceConfiguration.Provider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[RasterDataSourceConfiguration](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">RasterDataSourceConfiguration.Provider</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Configuration of a data provider.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#hasAlphaChannel"
  class="member-name-link"><code>hasAlphaChannel</code></a></td>
  <td><div class="block">
  A flag indicating whether the image content contains an alpha channel
  for transparency.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#headers"
  class="member-name-link"><code>headers</code></a></td>
  <td><div class="block">
  The optional name-value pairs specifying HTTP headers that are passed
  with each tile request.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#storageLevels"
  class="member-name-link"><code>storageLevels</code></a></td>
  <td><div class="block">
  The storage levels available for this data source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme"
  title="enum class in com.here.sdk.mapview.datasource"><code>TilingScheme</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#tilingScheme"
  class="member-name-link"><code>tilingScheme</code></a></td>
  <td><div class="block">
  The tiling scheme used by this source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback"
  title="interface in com.here.sdk.mapview.datasource"><code>TileUrlProviderCallback</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider#urlProvider"
  class="member-name-link"><code>urlProvider</code></a></td>
  <td><div class="block">
  Provides a function that generates URLs based on tile coordinates and
  storage level.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>Provider(TileUrlProviderCallback urlProvider,
   TilingScheme tilingScheme,
   List&lt;Integer&gt; storageLevels)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>Provider(TileUrlProviderCallback urlProvider,
   TilingScheme tilingScheme,
   List&lt;Integer&gt; storageLevels,
   boolean hasAlphaChannel,
   Map&lt;String,String&gt; headers)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

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

- <div id="field-detail" class="section field-details">

  - <div id="urlProvider" class="section detail">

    ### urlProvider

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TileUrlProviderCallback](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource")</span> <span class="element-name">urlProvider</span>

    </div>

    <div class="block">

    Provides a function that generates URLs based on tile coordinates
    and storage level.

    </div>

    </div>

  - <div id="tilingScheme" class="section detail">

    ### tilingScheme

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">tilingScheme</span>

    </div>

    <div class="block">

    The tiling scheme used by this source.

    </div>

    </div>

  - <div id="storageLevels" class="section detail">

    ### storageLevels

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>></span> <span class="element-name">storageLevels</span>

    </div>

    <div class="block">

    The storage levels available for this data source. Supported range
    \[0, 31\]. At least one level must be available for this provider to
    be used as a source of data. At storage level zero, the whole world
    is represented by one tile. At storage level 1 the world is split in
    2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The
    tiling process continues in this fashion until sufficient
    granularity has been achieved. In the XYZ addresing scheme for
    tiles, z value of the tile key coresponds to the storage level.
    Depending on the available storage levels and the given camera zoom
    level, the appropriate z value of the tile key will be determined.

    </div>

    </div>

  - <div id="hasAlphaChannel" class="section detail">

    ### hasAlphaChannel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAlphaChannel</span>

    </div>

    <div class="block">

    A flag indicating whether the image content contains an alpha
    channel for transparency. Default value is false .

    </div>

    </div>

  - <div id="headers" class="section detail">

    ### headers

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>></span> <span class="element-name">headers</span>

    </div>

    <div class="block">

    The optional name-value pairs specifying HTTP headers that are
    passed with each tile request.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List,boolean,java.util.Map)"
    class="section detail">

    ### Provider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Provider</span><span class="parameters">(@NonNull
    [TileUrlProviderCallback](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider,
    @NonNull
    [TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>> storageLevels,
    boolean hasAlphaChannel, @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> headers)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `urlProvider` -

    Provides a function that generates URLs based on tile coordinates
    and storage level.

    `tilingScheme` -

    The tiling scheme used by this source.

    `storageLevels` -

    The storage levels available for this data source. Supported range
    \[0, 31\]. At least one level must be available for this provider to
    be used as a source of data. At storage level zero, the whole world
    is represented by one tile. At storage level 1 the world is split in
    2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The
    tiling process continues in this fashion until sufficient
    granularity has been achieved. In the XYZ addresing scheme for
    tiles, z value of the tile key coresponds to the storage level.
    Depending on the available storage levels and the given camera zoom
    level, the appropriate z value of the tile key will be determined.

    `hasAlphaChannel` -

    A flag indicating whether the image content contains an alpha
    channel for transparency. Default value is `false`.

    `headers` -

    The optional name-value pairs specifying HTTP headers that are
    passed with each tile request.

    </div>

  - <div id="<init>(com.here.sdk.mapview.datasource.TileUrlProviderCallback,com.here.sdk.mapview.datasource.TilingScheme,java.util.List)"
    class="section detail">

    ### Provider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Provider</span><span class="parameters">(@NonNull
    [TileUrlProviderCallback](sdk-for-android-explore-com-here-sdk-mapview-datasource-tileurlprovidercallback "interface in com.here.sdk.mapview.datasource") urlProvider,
    @NonNull
    [TilingScheme](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilingscheme "enum class in com.here.sdk.mapview.datasource") tilingScheme,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a>> storageLevels)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `urlProvider` -

    Provides a function that generates URLs based on tile coordinates
    and storage level.

    `tilingScheme` -

    The tiling scheme used by this source.

    `storageLevels` -

    The storage levels available for this data source. Supported range
    \[0, 31\]. At least one level must be available for this provider to
    be used as a source of data. At storage level zero, the whole world
    is represented by one tile. At storage level 1 the world is split in
    2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The
    tiling process continues in this fashion until sufficient
    granularity has been achieved. In the XYZ addresing scheme for
    tiles, z value of the tile key coresponds to the storage level.
    Depending on the available storage levels and the given camera zoom
    level, the appropriate z value of the tile key will be determined.

    </div>

  </div>

</div>

