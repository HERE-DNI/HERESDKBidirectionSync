---
title: "MapView.TakeScreenshotCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapView.TakeScreenshotCallback

Enclosing class:
[MapView](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public static interface MapView.TakeScreenshotCallback
Callback to be called on retrieval of screenshot. In case of any error passed result is null.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onScreenshotTaken](#onScreenshotTaken(android.graphics.Bitmap))`(android.graphics.Bitmap bitmap)`

Callback to be called when screenshot is ready.

## Method Details

### onScreenshotTaken

void onScreenshotTaken(@Nullable android.graphics.Bitmap bitmap)

    Callback to be called when screenshot is ready.
Parameters:
    `bitmap` - The bitmap containing the screenshot.
