---
title: "MapView.OnReadyListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapview-onreadylistener"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapView.OnReadyListener

Enclosing class:
[MapView](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapView.OnReadyListener
Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map.

Whenever there is a need to call any map view related functions directly after the `Activity` resumes, [`onMapViewReady()`](#onMapViewReady()) should be used for this purpose, as it guarantees that those operations will work. It is not recommended to call map view functionality directly from `Activity`'s `onResume()`.

There are few typical moments in the lifecycle where it's useful to execute map view related operations:

- After map is shown for the very first time - use [`MapScene.LoadSceneCallback`](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview") that is passed to [`MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)`](sdk-for-android-explore-api-reference-latestmapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)).
- After the Activity is resumed - use `OnReadyListener` that is registered from within [`MapScene.LoadSceneCallback`](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview") the first time map scene is loaded.
- Every time the Activity is resumed, including after the map scene is first loaded - this combines previous two cases. Use `OnReadyListener` that is registered right after MapView is created, but before map scene is loaded.
See Also:
- [`MapView.setOnReadyListener(OnReadyListener)`](sdk-for-android-explore-api-reference-latestmapview#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener))

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onMapViewReady](#onMapViewReady())`()`

Callback to be called when MapView is fully initialized and ready to handle all operations.

## Method Details

### onMapViewReady

void onMapViewReady()

    Callback to be called when MapView is fully initialized and ready to handle all operations.
