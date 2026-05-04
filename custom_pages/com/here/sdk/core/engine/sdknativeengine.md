---
title: "SDKNativeEngine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsdknativeengine"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SDKNativeEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.core.engine.SDKNativeEngine
------------------------------------------------------------------------
public final class SDKNativeEngine extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Holds internal services and configurations needed by various HERE SDK modules.

You can initialize the HERE SDK in two ways:

- Create a shared instance of the `SDKNativeEngine` with `SDKNativeEngine.makeSharedInstance()`.
- Create individual instances of the `SDKNativeEngine` via `SDKNativeEngine()`. Note that this does not automatically set a shared instance.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [SDKNativeEngine.PurgeMemoryStrategy](sdk-for-android-explore-api-reference-latestsdknativeengine-purgememorystrategy)

Enum representing a strategy to flush memory caches.

## Constructor Summary

Constructors

Constructor

  Description

  [SDKNativeEngine](#%3Cinit%3E(android.content.Context,com.here.sdk.core.engine.SDKOptions))`(android.content.Context androidContext, `[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")` options)`

Makes a new instance of SDKNativeEngine using supplied options.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [clearPersistentUsageStats](#clearPersistentUsageStats())`()`

Clear persistent storage for the HERE SDK [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine").

`void`

  [clearUsageStatsCache](#clearUsageStatsCache())`()`

Clear cache for the HERE SDK [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine").

`void`

  [dispose](#dispose())`()`

Stops pending requests and closes open files and databases .

`void`

  [enableUsageStats](#enableUsageStats(boolean))`(boolean enabled)`

Enable or disable [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine") for the HERE SDK.

`void`

  [getDeviceId](#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback))`(`[`DeviceIdCallback`](sdk-for-android-explore-api-reference-latestdeviceidcallback "interface in com.here.sdk.core.engine")` callback)`

The unique identifier assigned to the device for this application.

[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")

  [getOptions](#getOptions())`()`

Gets the options used by this instance of [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine").

`static `[`ParameterConfiguration`](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core")

  [getParameterConfig](#getParameterConfig())`()`

Gets the configuration for default values of parameters used in the HERE SDK.

[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)`<`[`PassThroughFeature`](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")`>`

  [getPassThroughFeatures](#getPassThroughFeatures())`()`

Gets the pass through features.

[`ProxySettings`](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine")

  [getProxySettings](#getProxySettings())`()`

Gets the current proxy settings.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine")`>`

  [getSdkUsageStats](#getSdkUsageStats())`()`

Gets a list of usage statistics for all available HERE SDK features.

`static `[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")

  [getSharedInstance](#getSharedInstance())`()`

Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

`boolean`

  [isOfflineMode](#isOfflineMode())`()`

Gets the current offline mode.

`static void`

  [makeSharedInstance](#makeSharedInstance(android.content.Context,com.here.sdk.core.engine.SDKOptions))`(android.content.Context androidContext, `[`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")` options)`

Makes a new instance of this class using the supplied options and stores it as shared instance see [`getSharedInstance()`](#getSharedInstance()).

`void`

  [purgeMemoryCaches](#purgeMemoryCaches(com.here.sdk.core.engine.SDKNativeEngine.PurgeMemoryStrategy))`(`[`SDKNativeEngine.PurgeMemoryStrategy`](sdk-for-android-explore-api-reference-latestsdknativeengine-purgememorystrategy "enum class in com.here.sdk.core.engine")` strategy)`

Releases memory occupied by internal caches.

`void`

  [setAccessKeySecret](#setAccessKeySecret(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` accessKeySecret)`

Overrides HERE SDK access key secret with new value.

`void`

  [setAccessScope](#setAccessScope(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` scope)`

Overrides the token scope of the HERE SDK with new value.

`void`

  [setOfflineMode](#setOfflineMode(boolean))`(boolean value)`

Sets the offline mode.

`static void`

  [setParameterConfig](#setParameterConfig(com.here.sdk.core.ParameterConfiguration))`(`[`ParameterConfiguration`](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core")` value)`

Sets the configuration for default values of parameters used in the HERE SDK.

`void`

  [setPassThroughFeatures](#setPassThroughFeatures(java.util.Set))`(`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)`<`[`PassThroughFeature`](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")`> value)`

Sets the pass through features.

`void`

  [setProxySettings](#setProxySettings(com.here.sdk.core.engine.ProxySettings))`(`[`ProxySettings`](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine")` value)`

Sets the proxy settings.

`static void`

  [setSharedInstance](#setSharedInstance(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` value)`

Sets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (android.content.Context,com.here.sdk.core.engine.SDKOptions)" class="section detail">

### SDKNativeEngine

public SDKNativeEngine(@NonNull android.content.Context androidContext, @NonNull [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") options) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Makes a new instance of SDKNativeEngine using supplied options.
Parameters:
    `androidContext` -

    The Android context

    `options` -

    The options for the new engine.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### setAccessKeySecret

public void setAccessKeySecret(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) accessKeySecret)

    Overrides HERE SDK access key secret with new value. The new credentials will be used for new requests.

    **Note:** This method can be called from any thread. Access key ID can be set with constructor of SDKNativeEngine. New instance of SDKNativeEngine should be used if a new access key ID is required.
Parameters:
    `accessKeySecret` -

    New access key secret.

### setAccessScope

public void setAccessScope(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) scope)

    Overrides the token scope of the HERE SDK with new value. A new token will be fetched with the set scope and used for future requests. Setting an empty string will fetch a token for the global scope.

    This method can be called from any thread.
Parameters:
    `scope` -

    New scope for token

### dispose

public void dispose()

    Stops pending requests and closes open files and databases . Dispose signal is sent to dependent modules. Usage of engine, or dependent modules after calling dispose leads to undefined behavior. Please be aware that this method does not clean any type of storage. **Note:** This method should be called from main thread.

### enableUsageStats

public void enableUsageStats(boolean enabled)

    Enable or disable [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine") for the HERE SDK. Defaults to disabled (false). When enabled, `SDKNativeEngine.getSdkUsageStats()` returns actual online data consumption. Note that the flag does not cancel pending requests. [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine") can be enabled or disabled at any time.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `enabled` -

    True, if UsageStats are enabled.

### makeSharedInstance

public static void makeSharedInstance(@NonNull android.content.Context androidContext, @NonNull [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") options) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Makes a new instance of this class using the supplied options and stores it as shared instance see [`getSharedInstance()`](#getSharedInstance()). If there was a previously shared instance then it's disposed (so there is no need to call [`dispose()`](#dispose()) on app side) before the new instance is created.

    **Note:** The HERE SDK is not guaranteed to be thread safe and it is required to make calls to the SDK - including this one - from the main thread.
Parameters:
    `androidContext` -

    The Android context

    `options` -

    The options for the new engine.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

### clearPersistentUsageStats

public void clearPersistentUsageStats()

    Clear persistent storage for the HERE SDK [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine"). Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### clearUsageStatsCache

public void clearUsageStatsCache()

    Clear cache for the HERE SDK [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine"). Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### purgeMemoryCaches

public void purgeMemoryCaches(@NonNull [SDKNativeEngine.PurgeMemoryStrategy](sdk-for-android-explore-api-reference-latestsdknativeengine-purgememorystrategy "enum class in com.here.sdk.core.engine") strategy)

    Releases memory occupied by internal caches. Purging caches reduces memory footprint of application and may temporary reduce performance.
Parameters:
    `strategy` -

    Option to control how much memory caches will be purged.

### getDeviceId

public void getDeviceId(@NonNull [DeviceIdCallback](sdk-for-android-explore-api-reference-latestdeviceidcallback "interface in com.here.sdk.core.engine") callback)

    The unique identifier assigned to the device for this application. This device ID is primarily used for tracking Monthly Active Users (MAUs).
Parameters:
    `callback` -

    Callback which receives the result on the main thread.

### getOptions

@NonNull public [SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") getOptions()

    Gets the options used by this instance of [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine").
Returns:
    Options used by this instance of [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine").

### getSharedInstance

@Nullable public static [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") getSharedInstance()

    Gets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

    This is automatically set as a part of the SDK initialization process.
Returns:
    Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

### setSharedInstance

public static void setSharedInstance(@Nullable [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") value)

    Sets the shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

    This is automatically set as a part of the SDK initialization process.
Parameters:
    `value` -

    Shared instance of this SDK engine that can be accessed by any HERE SDK module as the default engine.

### isOfflineMode

public boolean isOfflineMode()

    Gets the current offline mode.

    Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See [`getPassThroughFeatures()`](#getPassThroughFeatures()). Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via [`SDKOptions.offlineMode`](sdk-for-android-explore-api-reference-latestsdkoptions#offlineMode). Initialization of the HERE SDK itself does not require an internet connection. Returns `true` if the HERE SDK uses offline connection mode, otherwise returns `false`.

    Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Returns:
    The offline mode.

### setOfflineMode

public void setOfflineMode(boolean value)

    Sets the offline mode.

    Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See [`getPassThroughFeatures()`](#getPassThroughFeatures()). Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via [`SDKOptions.offlineMode`](sdk-for-android-explore-api-reference-latestsdkoptions#offlineMode). Initialization of the HERE SDK itself does not require an internet connection. Returns `true` if the HERE SDK uses offline connection mode, otherwise returns `false`.

    Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `value` -

    The offline mode.

### getPassThroughFeatures

@Nullable public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)\<[PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")\> getPassThroughFeatures()

    Gets the pass through features.

    Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine") will be enabled when at least one pass-through feature is set.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Returns:
    The pass through features.

### setPassThroughFeatures

public void setPassThroughFeatures(@Nullable [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)\<[PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")\> value)

    Sets the pass through features.

    Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine") will be enabled when at least one pass-through feature is set.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `value` -

    The pass through features.

### getParameterConfig

@NonNull public static [ParameterConfiguration](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core") getParameterConfig()

    Gets the configuration for default values of parameters used in the HERE SDK.

    **Note:** This feature is in beta state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Returns:
    Configuration for default values of parameters used in the HERE SDK.

### setParameterConfig

public static void setParameterConfig(@NonNull [ParameterConfiguration](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core") value)

    Sets the configuration for default values of parameters used in the HERE SDK.

    **Note:** This feature is in beta state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `value` -

    Configuration for default values of parameters used in the HERE SDK.

### getProxySettings

@Nullable public [ProxySettings](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine") getProxySettings()

    Gets the current proxy settings.

    Defaults to (`null`), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (`null`) to indicate that proxy should be disabled. If proxy is necessary from the start then it's recommended to use [`NetworkSettings.proxySettings`](sdk-for-android-explore-api-reference-latestnetworksettings#proxySettings) in [`SDKOptions.networkSettings`](sdk-for-android-explore-api-reference-latestsdkoptions#networkSettings).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Returns:
    Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.

### setProxySettings

public void setProxySettings(@Nullable [ProxySettings](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine") value)

    Sets the proxy settings.

    Defaults to (`null`), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (`null`) to indicate that proxy should be disabled. If proxy is necessary from the start then it's recommended to use [`NetworkSettings.proxySettings`](sdk-for-android-explore-api-reference-latestnetworksettings#proxySettings) in [`SDKOptions.networkSettings`](sdk-for-android-explore-api-reference-latestsdkoptions#networkSettings).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `value` -

    Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.

### getSdkUsageStats

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[UsageStats](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine")\> getSdkUsageStats()

    Gets a list of usage statistics for all available HERE SDK features.

    [`UsageStats`](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine") has cache and persistent storage. Reads from the persistent storage happen on `SDKNativeEngine` creation step. Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Returns:
    Gets a list of usage statistics for all available HERE SDK features.
