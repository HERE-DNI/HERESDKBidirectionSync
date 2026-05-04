---
title: "RasterDataSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrasterdatasource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RasterDataSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.RasterDataSource
------------------------------------------------------------------------
public final class RasterDataSource extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Data source to load map layers using a raster image format (jpg, png). The example below illustrates how to create a raster data source and how to link it to a newly created map layer.

     RasterDataSource rasterDataSource = new RasterDataSource(mapContext, rasterDataSourceConfig);

        MapLayer layer = new MapLayerBuilder()
           // The name and the type of the data source have to be provided.
           // In our case, the name of the raster data source is in rasterDataSourceConfig.
           .withDataSource(rasterDataSourceConfig.name, MapContentType.RASTER_IMAGE)
           .forMap(map)
           .withName("rasterLayer")
           .build();

## Constructor Summary

Constructors

Constructor

  Description

  [RasterDataSource](#%3Cinit%3E(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context, `[`RasterDataSourceConfiguration`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")` configuration)`

Creates a RasterDataSource instance with the provided data source configuration.

[RasterDataSource](#%3Cinit%3E(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context, `[`RasterDataSourceConfiguration`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")` configuration, `[`RasterDataSourceListener`](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource")` listener)`

Creates a RasterDataSource instance with the provided data source configuration and registers a listener.

[RasterDataSource](#%3Cinit%3E(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`RasterTileSource`](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource")` tileSource)`

Creates a RasterDataSource instance with the provided raster tile source.

[RasterDataSource](#%3Cinit%3E(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`RasterTileSource`](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource")` tileSource, `[`RasterDataSourceListener`](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource")` listener)`

Creates a RasterDataSource instance with the provided raster tile source and registers a listener.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [addListener](#addListener(com.here.sdk.mapview.datasource.RasterDataSourceListener))`(`[`RasterDataSourceListener`](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource")` listener)`

Add listener for receiving state notifications.

`void`

  [changeConfiguration](#changeConfiguration(com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate))`(`[`RasterDataSourceConfigurationUpdate`](sdk-for-android-explore-api-reference-latestrasterdatasourceconfigurationupdate "class in com.here.sdk.mapview.datasource")` configuration)`

Applies the configuration update to the data source.

`void`

  [destroy](#destroy())`()`

Frees all internally used resources.

`void`

  [removeListener](#removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener))`(`[`RasterDataSourceListener`](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource")` listener)`

Remove a listener from receiving state notifications.

`void`

  [removeListeners](#removeListeners())`()`

Remove all listeners from receiving state notifications.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration)" class="section detail">

### RasterDataSource

public RasterDataSource(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context, @NonNull [RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource") configuration)

    Creates a RasterDataSource instance with the provided data source configuration.
Parameters:
    `context` -

    The map context to associate the data source with.

    `configuration` -

    The data source configuration object to use.
- (com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener)" class="section detail">

### RasterDataSource

public RasterDataSource(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context, @NonNull [RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource") configuration, @NonNull [RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)

    Creates a RasterDataSource instance with the provided data source configuration and registers a listener.
Parameters:
    `context` -

    The map context to associate the data source with.

    `configuration` -

    The data source configuration object to use.

    `listener` -

    The initial listener to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the listeners registered later might miss some notifications. This listener is guaranteed to receive all notifications.
- (com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource)" class="section detail">

### RasterDataSource

public RasterDataSource(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [RasterTileSource](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource") tileSource)

    Creates a RasterDataSource instance with the provided raster tile source. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `context` -

    The map context to associate the data source with.

    `name` -

    The unique name of the data source.

    `tileSource` -

    The raster tile source.
- (com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener)" class="section detail">

### RasterDataSource

public RasterDataSource(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [RasterTileSource](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource") tileSource, @NonNull [RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)

    Creates a RasterDataSource instance with the provided raster tile source and registers a listener. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `context` -

    The map context to associate the data source with.

    `name` -

    The unique name of the data source.

    `tileSource` -

    The raster tile source.

    `listener` -

    The initial listener to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the listeners registered later might miss some notifications. This listener is guaranteed to receive all notifications.

## Method Details

### changeConfiguration

public void changeConfiguration(@NonNull [RasterDataSourceConfigurationUpdate](sdk-for-android-explore-api-reference-latestrasterdatasourceconfigurationupdate "class in com.here.sdk.mapview.datasource") configuration)

    Applies the configuration update to the data source. An example for a configuration update is the update to a new bearer token for authentication.
Parameters:
    `configuration` -

    The data source configuration update to apply.

### addListener

public void addListener(@NonNull [RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)

    Add listener for receiving state notifications. The new listener is appended to the set of data source listeners as a strong reference and will receive only the notifications occurring after the registration. Caller is responsible for releasing the strong reference by calling [`removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)`](#removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)).
Parameters:
    `listener` -

    Listener to be added for receiving state notifications.

### removeListener

public void removeListener(@NonNull [RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource") listener)

    Remove a listener from receiving state notifications.
Parameters:
    `listener` -

    Listener to be removed from receiving state notifications.

### removeListeners

public void removeListeners()

    Remove all listeners from receiving state notifications.

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
