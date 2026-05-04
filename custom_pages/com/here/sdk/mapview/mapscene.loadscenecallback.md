---
title: "MapScene.LoadSceneCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapScene.LoadSceneCallback

Enclosing class:
[MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapScene.LoadSceneCallback
Called on the main thread after `loadScene()` method finishes loading the scene.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onLoadScene](#onLoadScene(com.here.sdk.mapview.MapError))`(`[`MapError`](sdk-for-android-explore-api-reference-latestmaperror "enum class in com.here.sdk.mapview")` loadSceneError)`

Called on the main thread after `loadScene()` method finishes loading the scene.

## Method Details

### onLoadScene

void onLoadScene(@Nullable [MapError](sdk-for-android-explore-api-reference-latestmaperror "enum class in com.here.sdk.mapview") loadSceneError)

    Called on the main thread after `loadScene()` method finishes loading the scene.
Parameters:
    `loadSceneError` -

    The load scene error
