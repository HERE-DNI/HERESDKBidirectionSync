---
title: "HereMap (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestheremap"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class HereMap

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.HereMap
------------------------------------------------------------------------
public final class HereMap extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
The representation of a dynamic and interactive geographic map. The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area. The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [addMapIdleListener](#addMapIdleListener(com.here.sdk.mapview.MapIdleListener))`(`[`MapIdleListener`](sdk-for-android-explore-api-reference-latestmapidlelistener "interface in com.here.sdk.mapview")` listener)`

Adds a listener for receiving idle state notifications and notifies it of the current state.

[`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")

  [getStyle](#getStyle())`()`

Gets the style that the map uses to customize the visual appearance of rendered features.

`void`

  [removeMapIdleListener](#removeMapIdleListener(com.here.sdk.mapview.MapIdleListener))`(`[`MapIdleListener`](sdk-for-android-explore-api-reference-latestmapidlelistener "interface in com.here.sdk.mapview")` listener)`

Removes a listener from receiving idle state notifications.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### addMapIdleListener

public void addMapIdleListener(@NonNull [MapIdleListener](sdk-for-android-explore-api-reference-latestmapidlelistener "interface in com.here.sdk.mapview") listener)

    Adds a listener for receiving idle state notifications and notifies it of the current state.

    The first notification received is always the state at the time of registration.

    The new listener is appended to the set of `HereMap` idle listeners as a strong reference. The caller is responsible for releasing the strong reference by calling [`removeMapIdleListener(com.here.sdk.mapview.MapIdleListener)`](#removeMapIdleListener(com.here.sdk.mapview.MapIdleListener)).
Parameters:
    `listener` -

    The listener

### removeMapIdleListener

public void removeMapIdleListener(@NonNull [MapIdleListener](sdk-for-android-explore-api-reference-latestmapidlelistener "interface in com.here.sdk.mapview") listener)

    Removes a listener from receiving idle state notifications.
Parameters:
    `listener` -

    The listener

### getStyle

@NonNull public [Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") getStyle()

    Gets the style that the map uses to customize the visual appearance of rendered features.

    Changes made to the map style using [`Style.update(com.here.sdk.mapview.Style)`](sdk-for-android-explore-api-reference-lateststyle#update(com.here.sdk.mapview.Style)) are lost when new scene is loaded using [`MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)`](sdk-for-android-explore-api-reference-latestmapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)) and its variants as well as when map features are enabled or disabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) and [`MapScene.disableFeatures(java.util.List<java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#disableFeatures(java.util.List)).

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Returns:
    The style that the map uses to customize the visual appearance of rendered features.
