---
title: "MapSceneLights.AttributeSettingCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapSceneLights.AttributeSettingCallback

Enclosing class:
[MapSceneLights](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapSceneLights.AttributeSettingCallback
This callback function allows handling errors that occur during the setting of light attributes.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onAttributeSetting](#onAttributeSetting(com.here.sdk.mapview.MapSceneLights.AttributeSettingError))`(`[`MapSceneLights.AttributeSettingError`](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingerror "enum class in com.here.sdk.mapview")` setLightError)`

This callback function allows handling errors that occur during the setting of light attributes.

## Method Details

### onAttributeSetting

void onAttributeSetting(@Nullable [MapSceneLights.AttributeSettingError](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingerror "enum class in com.here.sdk.mapview") setLightError)

    This callback function allows handling errors that occur during the setting of light attributes.
Parameters:
    `setLightError` -

    The cause for the failure when setting the light attributes, or `null` if no error occurred.

    Note: The error code `NO_LIGHTS` may be returned when attempting to set light attributes in map schemes that do not support lights, for instance `road.network` map scheme.

    Please refer to the error code documentation for further details on error handling.
