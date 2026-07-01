---
title: "RasterDataSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasource"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.RasterDataSource →
com.here.NativeBase → com.here.sdk.mapview.datasource.RasterDataSource

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RasterDataSource</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Data source to load map layers using a raster image format (jpg, png).
The example below illustrates how to create a raster data source and how
to link it to a newly created map layer. RasterDataSource
rasterDataSource = new RasterDataSource(mapContext,
rasterDataSourceConfig); MapLayer layer = new MapLayerBuilder() // The
name and the type of the data source have to be provided. // In our
case, the name of the raster data source is in rasterDataSourceConfig.
.withDataSource(rasterDataSourceConfig.name,
MapContentType.RASTER_IMAGE) .forMap(map) .withName("rasterLayer")
.build();

</div>

</div>

<div class="section summary">

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
  <td><pre><code>RasterDataSource(MapContext context,
   RasterDataSourceConfiguration configuration)</code></pre></td>
  <td><div class="block">
  Creates a RasterDataSource instance with the provided data source
  configuration.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>RasterDataSource(MapContext context,
   RasterDataSourceConfiguration configuration,
   RasterDataSourceListener listener)</code></pre></td>
  <td><div class="block">
  Creates a RasterDataSource instance with the provided data source
  configuration and registers a listener.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>RasterDataSource(MapContext context,
   String name,
   RasterTileSource tileSource)</code></pre></td>
  <td><div class="block">
  Creates a RasterDataSource instance with the provided raster tile
  source.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>RasterDataSource(MapContext context,
   String name,
   RasterTileSource tileSource,
   RasterDataSourceListener listener)</code></pre></td>
  <td><div class="block">
  Creates a RasterDataSource instance with the provided raster tile source
  and registers a listener.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addListener(RasterDataSourceListener listener)</code></pre></td>
  <td><div class="block">
  Add listener for receiving state notifications.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>changeConfiguration(RasterDataSourceConfigurationUpdate configuration)</code></pre></td>
  <td><div class="block">
  Applies the configuration update to the data source.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>destroy()</code></pre></td>
  <td><div class="block">
  Frees all internally used resources.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeListener(RasterDataSourceListener listener)</code></pre></td>
  <td><div class="block">
  Remove a listener from receiving state notifications.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeListeners()</code></pre></td>
  <td><div class="block">
  Remove all listeners from receiving state notifications.
  </div></td>
  </tr>
  </tbody>
  </table>

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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration)"
    class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><span class="parameters">(@NonNull
    [MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") context,
    @NonNull
    [RasterDataSourceConfiguration](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource") configuration)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided data source
    configuration.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `configuration` -

    The data source configuration object to use.

    </div>

  - <div id="<init>(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener)"
    class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><span class="parameters">(@NonNull
    [MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") context,
    @NonNull
    [RasterDataSourceConfiguration](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource") configuration,
    @NonNull
    [RasterDataSourceListener](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided data source
    configuration and registers a listener.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `configuration` -

    The data source configuration object to use.

    `listener` -

    The initial listener to be registered for receiving state
    notifications. Due to the asynchronous nature of the data source
    initialization, the listeners registered later might miss some
    notifications. This listener is guaranteed to receive all
    notifications.

    </div>

  - <div id="<init>(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource)"
    class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><span class="parameters">(@NonNull
    [MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") context,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [RasterTileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource "interface in com.here.sdk.mapview.datasource") tileSource)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided raster tile
    source. Note: This is a beta release of this feature, so there could
    be a few bugs and unexpected behavior. Related APIs may change for
    new releases without a deprecation process.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `name` -

    The unique name of the data source.

    `tileSource` -

    The raster tile source.

    </div>

  - <div id="<init>(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener)"
    class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><span class="parameters">(@NonNull
    [MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") context,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [RasterTileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-rastertilesource "interface in com.here.sdk.mapview.datasource") tileSource,
    @NonNull
    [RasterDataSourceListener](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided raster tile
    source and registers a listener. Note: This is a beta release of
    this feature, so there could be a few bugs and unexpected behavior.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `name` -

    The unique name of the data source.

    `tileSource` -

    The raster tile source.

    `listener` -

    The initial listener to be registered for receiving state
    notifications. Due to the asynchronous nature of the data source
    initialization, the listeners registered later might miss some
    notifications. This listener is guaranteed to receive all
    notifications.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="changeConfiguration(com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate)"
    class="section detail">

    ### changeConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">changeConfiguration</span><span class="parameters">(@NonNull
    [RasterDataSourceConfigurationUpdate](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate "class in com.here.sdk.mapview.datasource") configuration)</span>

    </div>

    <div class="block">

    Applies the configuration update to the data source. An example for
    a configuration update is the update to a new bearer token for
    authentication.

    </div>

    Parameters:  
    `configuration` -

    The data source configuration update to apply.

    </div>

  - <div id="addListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)"
    class="section detail">

    ### addListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addListener</span><span class="parameters">(@NonNull
    [RasterDataSourceListener](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)</span>

    </div>

    <div class="block">

    Add listener for receiving state notifications. The new listener is
    appended to the set of data source listeners as a strong reference
    and will receive only the notifications occurring after the
    registration. Caller is responsible for releasing the strong
    reference by calling
    removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)
    .

    </div>

    Parameters:  
    `listener` -

    Listener to be added for receiving state notifications.

    </div>

  - <div id="removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)"
    class="section detail">

    ### removeListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListener</span><span class="parameters">(@NonNull
    [RasterDataSourceListener](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)</span>

    </div>

    <div class="block">

    Remove a listener from receiving state notifications.

    </div>

    Parameters:  
    `listener` -

    Listener to be removed from receiving state notifications.

    </div>

  - <div id="removeListeners()" class="section detail">

    ### removeListeners

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListeners</span>()

    </div>

    <div class="block">

    Remove all listeners from receiving state notifications.

    </div>

    </div>

  - <div id="destroy()" class="section detail">

    ### destroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()

    </div>

    <div class="block">

    Frees all internally used resources. After calling this method, the
    object is not usable anymore.

    </div>

    </div>

  </div>

</div>

