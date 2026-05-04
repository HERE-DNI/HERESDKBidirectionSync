---
title: "MapSceneLights (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscenelights"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapSceneLights

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapSceneLights
------------------------------------------------------------------------
public final class MapSceneLights extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Manage the lights and their attributes in a scene.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback)

This callback function allows handling errors that occur during the setting of light attributes.

`static enum `

  [MapSceneLights.AttributeSettingError](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingerror)

Error enum indicating reasons for failure when setting light attributes.

`static enum `

  [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category)

The scene uses three categories of lighting which are: Main light, Back light and Rim light.

`static final class `

  [MapSceneLights.Direction](sdk-for-android-explore-api-reference-latestmapscenelights-direction)

The direction of lights as a pair of azimuth and altitude angles.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [getColor](#getColor(com.here.sdk.mapview.MapSceneLights.Category))`(`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")` category)`

Retrieves the current color of the light based on its category.

[`MapSceneLights.Direction`](sdk-for-android-explore-api-reference-latestmapscenelights-direction "class in com.here.sdk.mapview")

  [getDirection](#getDirection(com.here.sdk.mapview.MapSceneLights.Category))`(`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")` category)`

Retrieves the current direction of the light based on its category.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getIntensity](#getIntensity(com.here.sdk.mapview.MapSceneLights.Category))`(`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")` category)`

Retrieves the current intensity of the light based on its category.

`void`

  [reset](#reset())`()`

Resets all attributes of each light to their default values based on the current map scene settings.

`void`

  [setColor](#setColor(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.core.Color,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback))`(`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")` category, `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")` color, `[`MapSceneLights.AttributeSettingCallback`](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview")` callback)`

Set a new color for the light based on its category.

`void`

  [setDirection](#setDirection(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.mapview.MapSceneLights.Direction,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback))`(`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")` category, `[`MapSceneLights.Direction`](sdk-for-android-explore-api-reference-latestmapscenelights-direction "class in com.here.sdk.mapview")` direction, `[`MapSceneLights.AttributeSettingCallback`](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview")` callback)`

Set a new direction for the light based on its category.

`void`

  [setIntensity](#setIntensity(com.here.sdk.mapview.MapSceneLights.Category,double,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback))`(`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")` category, double intensity, `[`MapSceneLights.AttributeSettingCallback`](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview")` callback)`

Set a new intensity for the light based on its category.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### setColor

public void setColor(@NonNull [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") category, @NonNull [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") color, @Nullable [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview") callback)

    Set a new color for the light based on its category.
Parameters:
    `category` -

    The category of light for which the color is set.

    `color` -

    The Color type includes red, green, blue, and alpha components. The value of these components must be inside the range \[0, 1\].

    `callback` -

    Optional callback that will receive the result of this operation.

### setIntensity

public void setIntensity(@NonNull [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") category, double intensity, @Nullable [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview") callback)

    Set a new intensity for the light based on its category.
Parameters:
    `category` -

    The category of light for which the intensity is set.

    `intensity` -

    The light intensity value must be inside the range \[0, 10\]. The intensity value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Note: When the intensity value is big, 3D objects might turn completely white because all the color channels could go over the limit of 1.0.

    `callback` -

    Optional callback that will receive the result of this operation.

### setDirection

public void setDirection(@NonNull [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") category, @NonNull [MapSceneLights.Direction](sdk-for-android-explore-api-reference-latestmapscenelights-direction "class in com.here.sdk.mapview") direction, @Nullable [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview") callback)

    Set a new direction for the light based on its category.
Parameters:
    `category` -

    The category of light for which the direction is set.

    `direction` -

    The Direction contains azimuth and altitude angles in degrees.

    `callback` -

    Optional callback that will receive the result of this operation.

### getColor

@Nullable public [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") getColor(@NonNull [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") category)

    Retrieves the current color of the light based on its category.
Parameters:
    `category` -

    The category of light from which the color is retrieved.

    Returns:
    The current color of the light, or `null` if the light is missing from the loaded scene or MapScene is not intitialized.

### getIntensity

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getIntensity(@NonNull [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") category)

    Retrieves the current intensity of the light based on its category.
Parameters:
    `category` -

    The category of light from which the intensity is retrieved.

    Returns:
    The current intensity of the light, or `null` if the light is missing from the loaded scene or MapScene is not intitialized.

### getDirection

@Nullable public [MapSceneLights.Direction](sdk-for-android-explore-api-reference-latestmapscenelights-direction "class in com.here.sdk.mapview") getDirection(@NonNull [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") category)

    Retrieves the current direction of the light based on its category.
Parameters:
    `category` -

    The category of light from which the direction is retrieved.

    Returns:
    The current direction of the light, or `null` if the light is missing from the loaded scene or MapScene is not intitialized.

### reset

public void reset()

    Resets all attributes of each light to their default values based on the current map scene settings.
