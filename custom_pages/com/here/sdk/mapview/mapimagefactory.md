---
title: "MapImageFactory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapimagefactory"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapImageFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapImageFactory
------------------------------------------------------------------------
public class MapImageFactory extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Convenience factory class for loading marker resources from various sources.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [fromBitmap](#fromBitmap(android.graphics.Bitmap))`(android.graphics.Bitmap bitmap)`

Creates a map image from a supplied Bitmap.

`static `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [fromFile](#fromFile(java.lang.String,int,int))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` filePath, int width, int height)`

Creates a map image from a specified SVG Tiny or PNG file path.

`static `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [fromResource](#fromResource(android.content.res.Resources,int))`(android.content.res.Resources resources, int resourceID)`

Loads a map image from a specified bitmap resource ID.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### fromResource

public static [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") fromResource(android.content.res.Resources resources, int resourceID)

    Loads a map image from a specified bitmap resource ID. As usual on Android, the PNG format is preferred. Vector drawables are not supported.
Parameters:
    `resources` - the application's resources

    `resourceID` - resource ID for the bitmap image to load

    Returns:
    map image representing specified image resource

### fromFile

public static [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") fromFile(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filePath, int width, int height) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a map image from a specified SVG Tiny or PNG file path. Trying to load data not compliant to SVG Tiny or PNG might result in undefined behavior. This method needs read storage permission to be granted.
Parameters:
    `filePath` - the path pointing to SVG Tiny file

    `width` - preferred width

    `height` - preferred height

    Returns:
    map image representing specified image resource

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") - if dimension are invalid or path is empty.

### fromBitmap

public static [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") fromBitmap(@NonNull android.graphics.Bitmap bitmap)

    Creates a map image from a supplied Bitmap.
Parameters:
    `bitmap` - the bitmap image to use for creating the marker resource

    Returns:
    map image representing specified image resource
