---
title: "SDKOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsdkoptions"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SDKOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.SDKOptions
------------------------------------------------------------------------
public final class SDKOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine").

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock)

Action on cache lock

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`SDKOptions.ActionOnCacheLock`](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")

  [actionOnCacheLock](#actionOnCacheLock)

Specifies action to perform when cache folder is locked by another process.

[`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")

  [authenticationMode](#authenticationMode)

Encapsulates Authentication method and parameters.

`boolean`

  [autoUpdateOfOnlineCache](#autoUpdateOfOnlineCache)

Parameter to enable automatic cache updates.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [billingTag](#billingTag)

Internal to HERE SDK.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [cachePath](#cachePath)

Path to be used for caching purposes.

`long`

  [cacheSizeInBytes](#cacheSizeInBytes)

Desired upper bound of application size in bytes.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`CatalogConfiguration`](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine")`>`

  [catalogConfigurations](#catalogConfigurations)

This field specifies how the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") should access, use and store data for different catalogs.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[`EngineBaseURL`](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine"), [`EngineOptions`](sdk-for-android-explore-api-reference-latestengineoptions "class in com.here.sdk.core.engine")`>`

  [customEngineOptions](#customEngineOptions)

Set custom options for SDK Engines.

[`Metadata`](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")

  [customOptions](#customOptions)

Options that define custom behavior for the HERE SDK.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [dataPath](#dataPath)

Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.

[`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine")

  [layerConfiguration](#layerConfiguration)

Defines a list of data features that can be enabled / disabled.

`boolean`

  [lowMemoryMode](#lowMemoryMode)

If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint.

[`NetworkSettings`](sdk-for-android-explore-api-reference-latestnetworksettings "class in com.here.sdk.core.engine")

  [networkSettings](#networkSettings)

Network settings to use at the start.

`boolean`

  [offlineMode](#offlineMode)

Sets offline mode for the HERE SDK.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [persistentMapStoragePath](#persistentMapStoragePath)

Path to store persistent map data.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [politicalView](#politicalView)

Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [scope](#scope)

Optional project ID to set the project scope of the login session.

## Constructor Summary

Constructors

Constructor

  Description

  [SDKOptions](#%3Cinit%3E(com.here.sdk.core.engine.AuthenticationMode))`(`[`AuthenticationMode`](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")` authenticationMode)`

Constructs a SDKOptions from authentication mode.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### scope

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) scope

    Optional project ID to set the project scope of the login session. Not used if empty. see also [Manage Projects](https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html) and [IAM Concepts](https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html)

### cachePath

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cachePath

    Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths: `Context.getCacheDir().getPath()` . If an absolute path is set, it will be used instead. If a relative path is set then directory `Context.getCacheDir().getPath()` is used as parent path. Note, The cache path should be located under [app-specific directory](https://developer.android.com/training/data-storage/app-specific). Using shared directories such as `Documents` is not recommended as it will expose HERE SDK files to the other apps. It will also require additional permissions such as `MANAGE_EXTERNAL_STORAGE` and results in a poorer HERE SDK performance overall. The recommended location in terms of file I/O speed is the app's internal storage directory, whereas an external SD card is expected to be slower. This also depends on the quality of the used SD card.

### cacheSizeInBytes

public long cacheSizeInBytes

    Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed. Default value 256MB

### dataPath

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dataPath

    Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.

    **Note:** For common use cases, prefer [`persistentMapStoragePath`](#persistentMapStoragePath), or keep the default paths. Use `dataPath` only as a fallback if [`persistentMapStoragePath`](#persistentMapStoragePath) is not writable, for example, when you have an agreement with HERE to flash data at factory time.

    By default, this returns an empty string. In this case, the same path as [`persistentMapStoragePath`](#persistentMapStoragePath) will be used. If an absolute path is set, it will be used instead. If a relative path is set then directory `Context.getFilesDir().getPath()` is used as parent path. Application must have read/write permissions to the given desired path. It is recommended that the application has exclusive access to this path. Avoid using shared or public directories such as `Download` or `Documents`. Using such directories may cause certain HERE SDK features to behave with limitations. For example, index creation for offline search may fail or not function as expected. It is recommended not to use the application cache paths like `Context.getCacheDir().getPath()` , since operating system manages data in this location and data can be deleted if the device is low on storage space, which will result in application malfunction. The path can be on internal or external storage. The internal storage is recommended due to the file I/O speed. Note: If the [`persistentMapStoragePath`](#persistentMapStoragePath) is writable, `dataPath` can be left empty. If the [`persistentMapStoragePath`](#persistentMapStoragePath) is not writable, `dataPath` must be set and also be writable. Note that `dataPath` is used to store essential HERE SDK data.

    **Important:** There is no automatic migration of stored data between the [`persistentMapStoragePath`](#persistentMapStoragePath) and the `dataPath`. For ease of management, it's recommended to set the persistence path as writable and ignore `dataPath`. If `dataPath` is set differently from the [`persistentMapStoragePath`](#persistentMapStoragePath), some data that would typically be saved in the [`persistentMapStoragePath`](#persistentMapStoragePath) will now be saved to `dataPath`. If `dataPath` is set and later unset, any data stored there will remain inaccessible and will not be migrated back.

### persistentMapStoragePath

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) persistentMapStoragePath

    Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths: `Context.getFilesDir().getPath()` . If an absolute path is set, it will be used instead. If a relative path is set then directory `Context.getFilesDir().getPath()` is used as parent path. **Note**: Offline maps stored at `<persistent_map_storage_path>/v1/<access_key_id>/ocm-map/`, where `<access_key_id>` is taken from `SDKOptions.authenticationMode`. When `SDKOptions` initialized with `AuthenticationMode.withToken` or `AuthenticationMode.withExternal`, then `<access_key_id>` left empty.

    Note, persistent map storage path should be located under [app-specific directory](https://developer.android.com/training/data-storage/app-specific). Using shared directories such as `Documents` is not recommended as it will expose HERE SDK files to the other apps. It will also require additional permissions such as `MANAGE_EXTERNAL_STORAGE` and results in a poorer HERE SDK performance overall. Additionally, the Android MediaProvider imposes certain restrictions on the creation of non-media files (such as temporary files or database files), which may cause some functionality to not behave as expected. The recommended location in terms of file I/O speed is the app's internal storage directory, whereas an external SD card is expected to be slower. This also depends on the quality of the used SD card.

    Note: If the persistent map storage location has the read only permission, then the [`dataPath`](#dataPath) must be configured.

### politicalView

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) politicalView

    Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has an international and an alternative geopolitical view. When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.

    Note: Defaults to an empty string which enables the international view.

    This is a beta feature and thus there can be bugs and unexpected behavior.

### offlineMode

public boolean offlineMode

    Sets offline mode for the HERE SDK. Defaults to `false`. When enabled, this prevents the HERE SDK from initiating any online connection from starting. The mode can be disabled or enabled again at any time via [`SDKNativeEngine.isOfflineMode()`](sdk-for-android-explore-api-reference-latestsdknativeengine#isOfflineMode()).

### layerConfiguration

@NonNull public [LayerConfiguration](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") layerConfiguration

    Defines a list of data features that can be enabled / disabled. Once set to [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") when a new HERE SDK is constructed, it will affect the map cache and offline maps. When disabling certain features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine"). However, for new map data, it will be applied. For offline maps, this [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") can reduce the download size of all regions. Note that the [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") is applied globally to all regions that will be downloaded in the future. It will not affect already downloaded regions. Updating a region will also not update the [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine"). Only the [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") will be used that was set globally when a region was downloaded for the first time. If you want to update the [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") for an already downloaded region, please delete the region and download it again.

    Please also note

    - The [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") is only applicable for the HERE SDK (Navigate) that contains the offline maps feature. It has no effect on other licenses.
    - The [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.
    - It is not possible to specify a separate [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") for the map cache and offline maps. The [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") will be always applied to both.
    - The [`LayerConfiguration`](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine") does affect the map cache when a device has connectivity. Even when a device has connectivity it will only download the specified layers.
    - This is a beta feature and thus there can be bugs and unexpected behavior.

### catalogConfigurations

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[CatalogConfiguration](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine")\> catalogConfigurations

    This field specifies how the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") should access, use and store data for different catalogs. You can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases. For further information about catalogs and related concepts see [`CatalogConfiguration`](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine")

    **Note:** This API is only available for the Navigate license. It has no affect on other license.

### autoUpdateOfOnlineCache

public boolean autoUpdateOfOnlineCache

    Parameter to enable automatic cache updates.

    When it is false, the cache will always use the same map version as offline maps. If offline maps are updated, the cache will be also updated. The cache version will never be older than the offline maps version.

    When it is true, the cache will be automatically updated to use the latest map data that is available. In that case, the cache may contain map data that is newer than the offline maps data. Note that auto updates may also lead to increased network traffic, as the cached data will be evicted tile-by-tile before it is filled with newer map data. This process continues everytime the user views a new map view area until the data is replaced. Once also the offline map data is updated by the user, both map versions will be the same again.

    If the value is also specified via the manifest (Android) or plist (iOS), than the value set via `SDKOptions` will overrule the value that was set in manifest/plist - until the current session ends and the value is read/set again.

    Note that offline maps are only available for the Navigate license.

    Defaults to `false`.

    **Note:** Do not use this yet, the behavior of this feature may be inconsistent. Once it will be usable, it will be announced in the regular HERE SDK release notes.

### customEngineOptions

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine"),[EngineOptions](sdk-for-android-explore-api-reference-latestengineoptions "class in com.here.sdk.core.engine")\> customEngineOptions

    Set custom options for SDK Engines. This includes:

    - `custom_base_url`: Allows engines to use custom base URLs for alternative services. By default, the available endpoints use HERE backend endpoints. If unsupported base URLs are specified, the related features will become non-functional. Please contact your HERE representative to learn about possible custom base URL usage options.
    - `custom_authentication_mode`: Enables bearer authentication mode for engines, which adds or omits the header ("Authorization", "Bearer \$Token") to each online request made by the module the object is added to. The token (if used) can be provided directly or retrieved via key/secret from a dedicated backend. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### actionOnCacheLock

@NonNull public [SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine") actionOnCacheLock

    Specifies action to perform when cache folder is locked by another process. Default value is [`SDKOptions.ActionOnCacheLock.WAIT_LOCKING_APP_FINISH`](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock#WAIT_LOCKING_APP_FINISH).

### authenticationMode

@NonNull public [AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") authenticationMode

    Encapsulates Authentication method and parameters.

### networkSettings

@NonNull public [NetworkSettings](sdk-for-android-explore-api-reference-latestnetworksettings "class in com.here.sdk.core.engine") networkSettings

    Network settings to use at the start. Some of those settings can be changed later.

### lowMemoryMode

public boolean lowMemoryMode

    If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint. When set to `true` configures internal memory caches to consume less memory. Reduction in cache sizes also reduces performance of the HERE SDK. In order to release memory occupied by internal caches see [`SDKNativeEngine.purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)`](sdk-for-android-explore-api-reference-latestsdknativeengine#purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy)).

### billingTag

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) billingTag

    Internal to HERE SDK. DO NOT USE THIS YET.

    **Warning:** This is a placeholder and under developement. We will announce its availability in our changelog once it is ready for use.

    A parameter to set a billing tag to track your HERE platform usage across the various HERE services your application may contact. For more information on the billing tag, see our [cost management guide](https://www.here.com/docs/bundle/cost-management-developer-guide/page/topics/tutorial-billing-tags.html). The tag needs to follow the format as described in the guide or it will be ignored. The parameter defaults to `null`, which also means that the tag is ignored for all requests.

    **Note:** The billing tag is optional, but when set, it can help you to understand how often your app uses certain services, for example, the number of hits to our HERE backend routing services. For more details on tracking such details, please consult the *cost management guide* or get in touch with the HERE billing team.

### customOptions

@Nullable public [Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core") customOptions

    Options that define custom behavior for the HERE SDK. These settings allow fine-tuning of internal thread pools and resource management for advanced use cases. These options are intended for *internal* usage only and should not be modified unless instructed by HERE support.

    Note: This is a *beta* release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Details

  - (com.here.sdk.core.engine.AuthenticationMode)" class="section detail">

### SDKOptions

public SDKOptions(@NonNull [AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine") authenticationMode)

    Constructs a SDKOptions from authentication mode. Other fields are filled with default values.
Parameters:
    `authenticationMode` -

    Authentication Mode used for obtaining an access token.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
