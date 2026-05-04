---
title: "MapSceneLoadOptionsBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapSceneLoadOptionsBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapSceneLoadOptionsBuilder
------------------------------------------------------------------------
public final class MapSceneLoadOptionsBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder for creating [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") instances. This builder ensures that either a MapScheme or a configuration file is set, but not both.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapSceneLoadOptionsBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationerrorcode)

Describes a reason for failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").

`static final class `

  [MapSceneLoadOptionsBuilder.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationerrordetails)

Describes the reason for failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").

`static final class `

  [MapSceneLoadOptionsBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationexception)

Thrown when failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").

## Constructor Summary

Constructors

Constructor

  Description

  [MapSceneLoadOptionsBuilder](#%3Cinit%3E())`()`

Creates a new builder instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview")

  [build](#build())`()`

Builds the [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") instance.

[`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  [withConfigurationFile](#withConfigurationFile(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` configurationFile)`

Sets the configuration file path to load.

[`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  [withDisabledFeatures](#withDisabledFeatures(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> disabledFeatures)`

Sets the features to disable in the new configuration.

[`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  [withEnabledFeatures](#withEnabledFeatures(java.util.Map))`(`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`> enabledFeatures)`

Sets the features to enable in the new configuration.

[`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  [withMapScheme](#withMapScheme(com.here.sdk.mapview.MapScheme))`(`[`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")` mapScheme)`

Sets the map scheme to load.

[`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  [withOverridingMapStyle](#withOverridingMapStyle(com.here.sdk.mapview.Style))`(`[`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")` overridingMapStyle)`

Sets the style to override what is defined in the scene configuration.

[`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  [withWatermarkStyle](#withWatermarkStyle(com.here.sdk.mapview.WatermarkStyle))`(`[`WatermarkStyle`](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview")` watermarkStyle)`

Sets the watermark style.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### MapSceneLoadOptionsBuilder

public MapSceneLoadOptionsBuilder()

    Creates a new builder instance.

## Method Details

### withMapScheme

@NonNull public [MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview") withMapScheme(@NonNull [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") mapScheme)

    Sets the map scheme to load. Any configuration file set through [`withConfigurationFile(java.lang.String)`](#withConfigurationFile(java.lang.String)) will be discarded.
Parameters:
    `mapScheme` -

    Map scheme to load.

    Returns:
    This class instance.

### withConfigurationFile

@NonNull public [MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview") withConfigurationFile(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) configurationFile)

    Sets the configuration file path to load. Any map scheme set through [`withMapScheme(com.here.sdk.mapview.MapScheme)`](#withMapScheme(com.here.sdk.mapview.MapScheme)) will be discarded.
Parameters:
    `configurationFile` -

    Configuration file path to load.

    Returns:
    This class instance.

### withEnabledFeatures

@NonNull public [MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview") withEnabledFeatures(@NonNull [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> enabledFeatures)

    Sets the features to enable in the new configuration.
Parameters:
    `enabledFeatures` -

    Features to enable. Key = feature name, value = mode name.

    Returns:
    This class instance.

### withDisabledFeatures

@NonNull public [MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview") withDisabledFeatures(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> disabledFeatures)

    Sets the features to disable in the new configuration.
Parameters:
    `disabledFeatures` -

    Features to disable.

    Returns:
    This class instance.

### withWatermarkStyle

@NonNull public [MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview") withWatermarkStyle(@NonNull [WatermarkStyle](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview") watermarkStyle)

    Sets the watermark style.
Parameters:
    `watermarkStyle` -

    Watermark style to use.

    Returns:
    This class instance.

### withOverridingMapStyle

@NonNull public [MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview") withOverridingMapStyle(@NonNull [Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") overridingMapStyle)

    Sets the style to override what is defined in the scene configuration.
Parameters:
    `overridingMapStyle` -

    Map style to override the scene configuration.

    Returns:
    This class instance.

### build

@NonNull public [MapSceneLoadOptions](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") build() throws [MapSceneLoadOptionsBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationexception "class in com.here.sdk.mapview")

    Builds the [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") instance.
Returns:
    A new MapSceneLoadOptions instance.

    Throws:
    [`MapSceneLoadOptionsBuilder.InstantiationException`](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.
