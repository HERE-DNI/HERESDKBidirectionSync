---
title: "MapLayer (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaplayer"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapLayer

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapLayer
------------------------------------------------------------------------
public final class MapLayer extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Interface for managing a map layer. A map layer can be created by using the [`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview"). At creation, the layer gets added to a map. The layer gets removed from the map upon instance destruction.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [destroy](#destroy())`()`

Frees all internally used resources.

`void`

  [setEnabled](#setEnabled(boolean))`(boolean enable)`

Sets whether or not the layer is enabled to be drawn.

`void`

  [setPriority](#setPriority(com.here.sdk.mapview.MapLayerPriority))`(`[`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")` priority)`

Sets the render priority for the layer which replaces any previously defined priorities.

`void`

  [setStyle](#setStyle(com.here.sdk.mapview.Style))`(`[`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")` style)`

Sets the style to be used by the layer.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### setEnabled

public void setEnabled(boolean enable)

    Sets whether or not the layer is enabled to be drawn.
Parameters:
    `enable` -

    `True` to enable the layer, `false` to disable it.

### setStyle

public void setStyle(@NonNull [Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") style)

    Sets the style to be used by the layer. For more details see Custom Layer Style Reference in the documentation. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `style` -

    Style for the layer.

### setPriority

public void setPriority(@NonNull [MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") priority)

    Sets the render priority for the layer which replaces any previously defined priorities.
Parameters:
    `priority` -

    Priority for the layer.

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
