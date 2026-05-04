---
title: "MapViewLifecycleListener (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapViewLifecycleListener

------------------------------------------------------------------------
public interface MapViewLifecycleListener
Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

A configuration change that results in `Activity` being recreated does not trigger an [`onDestroy()`](#onDestroy()) call. The listener will be preserved throughout the destruction and recreation of the MapView. It is safe to hold and use the `MapViewBase` object passed in [`onAttach(com.here.sdk.mapview.MapViewBase)`](#onAttach(com.here.sdk.mapview.MapViewBase)) until `onDetach()` or `onDestroy()` gets called. However, it is important that the listener *does not* hold a strong reference to an `Activity`, directly or indirectly (for example by holding a reference to a [`MapView`](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview"). A component implementing this interface should interact with the map view only through the `MapViewBase` object passed in [`onAttach(com.here.sdk.mapview.MapViewBase)`](#onAttach(com.here.sdk.mapview.MapViewBase)).

A `MapView` is using a [SurfaceView](https://developer.android.com/reference/android/view/SurfaceView)

to render its content.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onAttach](#onAttach(com.here.sdk.mapview.MapViewBase))`(`[`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")` mapView)`

Called when adding [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to the map view.

`void`

  [onDestroy](#onDestroy())`()`

Called when the map view to which this is attached to is destroyed.

`void`

  [onDetach](#onDetach(com.here.sdk.mapview.MapViewBase))`(`[`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")` mapView)`

Called when removing [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from the map view.

`void`

  [onPause](#onPause())`()`

Called when the map view to which this [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") is attached to gets paused (usually when the app goes into background).

`void`

  [onResume](#onResume())`()`

Called when the map view to which this [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") is attached to gets resumed (usually when the app goes into foreground).

## Method Details

### onAttach

void onAttach(@NonNull [MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview") mapView)

    Called when adding [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to the map view. If the map view does not have render target attached at the time of adding the listener, then this method will be called later, after render target is attached. This means that the map view it receives is always fully initialized.

    Can be used to implement the logic to create and add visual components to the map view.
Parameters:
    `mapView` -

    The map view to attach to.

### onDetach

void onDetach(@NonNull [MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview") mapView)

    Called when removing [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from the map view. Can be used to implement the logic to remove visual components from the map view and release resources if necessary.
Parameters:
    `mapView` -

    The map view to detach from.

### onPause

void onPause()

    Called when the map view to which this [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") is attached to gets paused (usually when the app goes into background). This should be used by components that perform continuous updates to pause those updates until [`onResume()`](#onResume()) is called.

### onResume

void onResume()

    Called when the map view to which this [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") is attached to gets resumed (usually when the app goes into foreground). This should be used by components that perform continuous updates to resume those updates after a previous call to [`onPause()`](#onPause()).

### onDestroy

void onDestroy()

    Called when the map view to which this is attached to is destroyed. After this is called, no other [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") method will be invoked. This should be used to make sure all resources are freed.
