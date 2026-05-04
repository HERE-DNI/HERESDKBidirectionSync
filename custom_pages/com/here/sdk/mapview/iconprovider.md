---
title: "IconProvider (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesticonprovider"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class IconProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.IconProvider
------------------------------------------------------------------------
public class IconProvider extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme. The icon creation currently does not rely on map data. Therefore, it works without online connection. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [IconProvider.IconCallback](sdk-for-android-explore-api-reference-latesticonprovider-iconcallback)

Interface which is used as callback to pass back an image or error code after calling the createRoadShieldIcon() method.

## Constructor Summary

Constructors

Constructor

  Description

  [IconProvider](#%3Cinit%3E(com.here.sdk.mapview.MapContext))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` mapContext)`

Creates an IconProvider.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [createRoadShieldIcon](#createRoadShieldIcon(com.here.sdk.mapview.RoadShieldIconProperties,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,long,long,com.here.sdk.mapview.IconProvider.IconCallback))`(`[`RoadShieldIconProperties`](sdk-for-android-explore-api-reference-latestroadshieldiconproperties "class in com.here.sdk.mapview")` properties, `[`MapScheme`](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")` mapScheme, `[`IconProviderAssetType`](sdk-for-android-explore-api-reference-latesticonproviderassettype "enum class in com.here.sdk.mapview")` assetType, long widthConstraintInPixels, long heightConstraintInPixels, `[`IconProvider.IconCallback`](sdk-for-android-explore-api-reference-latesticonprovider-iconcallback "interface in com.here.sdk.mapview")` callback)`

Creates an image displaying a road shield according to the given parameters.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapContext)" class="section detail">

### IconProvider

public IconProvider([MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") mapContext)

    Creates an IconProvider.
Parameters:
    `mapContext` - The map context instance.

## Method Details

### createRoadShieldIcon

public void createRoadShieldIcon(@NonNull [RoadShieldIconProperties](sdk-for-android-explore-api-reference-latestroadshieldiconproperties "class in com.here.sdk.mapview") properties, @NonNull [MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview") mapScheme, @NonNull [IconProviderAssetType](sdk-for-android-explore-api-reference-latesticonproviderassettype "enum class in com.here.sdk.mapview") assetType, long widthConstraintInPixels, long heightConstraintInPixels, @NonNull [IconProvider.IconCallback](sdk-for-android-explore-api-reference-latesticonprovider-iconcallback "interface in com.here.sdk.mapview") callback)

    Creates an image displaying a road shield according to the given parameters.
Parameters:
    `properties` - The properties which determine the kind of road shield to be created.

    `mapScheme` - The map scheme for which the road shield should be created.

    `assetType` - The asset type for which the road shield should be created.

    `widthConstraintInPixels` - The maximum width of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the width will be calculated based on the heightConstraintInPixels to preserve the aspect ratio.

    `heightConstraintInPixels` - The maximum height of the road shield in pixels. The value is capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If set to 0, the original image-asset's height will be used.

    `callback` - The callback which is used to return the created image or an error code. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
