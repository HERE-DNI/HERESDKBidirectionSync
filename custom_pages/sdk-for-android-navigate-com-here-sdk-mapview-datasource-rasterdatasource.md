---
title: "RasterDataSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.datasource.RasterDataSource → com.here.NativeBase com.here.sdk.mapview.datasource.RasterDataSource → com.here.sdk.mapview.datasource.RasterDataSource

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RasterDataSource</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Data source to load map layers using a raster image format (jpg, png). The example below illustrates how to create a raster data source and how to link it to a newly created map layer. RasterDataSource rasterDataSource = new RasterDataSource(mapContext, rasterDataSourceConfig); MapLayer layer = new MapLayerBuilder() // The name and the type of the data source have to be provided. // In our case, the name of the raster data source is in rasterDataSourceConfig. .withDataSource(rasterDataSourceConfig.name, MapContentType.RASTER_IMAGE) .forMap(map) .withName("rasterLayer") .build();

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      RasterDataSource ( MapContext context, RasterDataSourceConfiguration configuration)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a RasterDataSource instance with the provided data source configuration.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RasterDataSource ( MapContext context, RasterDataSourceConfiguration configuration, RasterDataSourceListener listener)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a RasterDataSource instance with the provided data source configuration and registers a listener.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RasterDataSource ( MapContext context, String name, RasterTileSource tileSource)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a RasterDataSource instance with the provided raster tile source.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RasterDataSource ( MapContext context, String name, RasterTileSource tileSource, RasterDataSourceListener listener)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a RasterDataSource instance with the provided raster tile source and registers a listener.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

      addListener ( RasterDataSourceListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Add listener for receiving state notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      changeConfiguration ( RasterDataSourceConfigurationUpdate configuration)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Applies the configuration update to the data source.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      destroy ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Frees all internally used resources.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeListener ( RasterDataSourceListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Remove a listener from receiving state notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeListeners ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Remove all listeners from receiving state notifications.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapview-MapContext-com-here-sdk-mapview-datasource-RasterDataSourceConfiguration" class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided data source configuration.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `configuration` -

    The data source configuration object to use.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapview-MapContext-com-here-sdk-mapview-datasource-RasterDataSourceConfiguration-com-here-sdk-mapview-datasource-RasterDataSourceListener" class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided data source configuration and registers a listener.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `configuration` -

    The data source configuration object to use.

    `listener` -

    The initial listener to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the listeners registered later might miss some notifications. This listener is guaranteed to receive all notifications.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapview-MapContext-java-lang-String-com-here-sdk-mapview-datasource-RasterTileSource" class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided raster tile source. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `name` -

    The unique name of the data source.

    `tileSource` -

    The raster tile source.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-mapview-MapContext-java-lang-String-com-here-sdk-mapview-datasource-RasterTileSource-com-here-sdk-mapview-datasource-RasterDataSourceListener" class="section detail">

    ### RasterDataSource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span>

    </div>

    <div class="block">

    Creates a RasterDataSource instance with the provided raster tile source and registers a listener. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `context` -

    The map context to associate the data source with.

    `name` -

    The unique name of the data source.

    `tileSource` -

    The raster tile source.

    `listener` -

    The initial listener to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the listeners registered later might miss some notifications. This listener is guaranteed to receive all notifications.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-changeConfiguration-com-here-sdk-mapview-datasource-RasterDataSourceConfigurationUpdate" class="section detail">

    ### changeConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">changeConfiguration</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfigurationUpdate</a> configuration)</span>

    </div>

    <div class="block">

    Applies the configuration update to the data source. An example for a configuration update is the update to a new bearer token for authentication.

    </div>

    Parameters:  
    `configuration` -

    The data source configuration update to apply.

    </div>

  - <div id="sdk-for-android-navigate-addListener-com-here-sdk-mapview-datasource-RasterDataSourceListener" class="section detail">

    ### addListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span>

    </div>

    <div class="block">

    Add listener for receiving state notifications. The new listener is appended to the set of data source listeners as a strong reference and will receive only the notifications occurring after the registration. Caller is responsible for releasing the strong reference by calling removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener) .

    </div>

    Parameters:  
    `listener` -

    Listener to be added for receiving state notifications.

    </div>

  - <div id="sdk-for-android-navigate-removeListener-com-here-sdk-mapview-datasource-RasterDataSourceListener" class="section detail">

    ### removeListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span>

    </div>

    <div class="block">

    Remove a listener from receiving state notifications.

    </div>

    Parameters:  
    `listener` -

    Listener to be removed from receiving state notifications.

    </div>

  - <div id="sdk-for-android-navigate-removeListeners" class="section detail">

    ### removeListeners

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListeners</span>()

    </div>

    <div class="block">

    Remove all listeners from receiving state notifications.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-destroy" class="section detail">

    ### destroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()

    </div>

    <div class="block">

    Frees all internally used resources. After calling this method, the object is not usable anymore.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

