---
title: "MapImage (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapimage"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapImage

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapImage
------------------------------------------------------------------------
public final class MapImage extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents a drawable resource that can be used by a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview"), [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") or [`MapImageOverlay`](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview") to be shown on the map. Supported formats are listed in [`ImageFormat`](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview"). SVG format allows custom fonts in text using font-family attribute by prior registration via `AssetsManager.registerFont`.

It is recommended to associate a resource with a single `MapImage` instance in order to enable resource sharing and reduce the amount of needed memory.

## Constructor Summary

Constructors

Constructor

  Description

  [MapImage](#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat))`(byte[] pixelData, `[`ImageFormat`](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview")` imageFormat)`

Creates a new map image from the provided image data.

[MapImage](#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat,long,long))`(byte[] imageData, `[`ImageFormat`](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview")` imageFormat, long width, long height)`

Creates a new map image from the provided image data.

[MapImage](#%3Cinit%3E(java.lang.String,long,long))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` filePath, long width, long height)`

Creates a new map image from the provided path to the SVG Tiny or PNG image.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (byte[],com.here.sdk.mapview.ImageFormat)" class="section detail">

### MapImage

public MapImage(@NonNull byte\[\] pixelData, @NonNull [ImageFormat](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview") imageFormat)

    Creates a new map image from the provided image data. Currently only [`ImageFormat.PNG`](sdk-for-android-explore-api-reference-latestimageformat#PNG) is accepted.
Parameters:
    `pixelData` -

    Data to be used for the image. The bytes of a PNG image datastream are expected as defined in https://www.w3.org/TR/PNG

    `imageFormat` -

    The format of the image data to be used.
- (byte[],com.here.sdk.mapview.ImageFormat,long,long)" class="section detail">

### MapImage

public MapImage(@NonNull byte\[\] imageData, @NonNull [ImageFormat](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview") imageFormat, long width, long height)

    Creates a new map image from the provided image data.
Parameters:
    `imageData` -

    Data to be used for the image. For image format [`ImageFormat.SVG`](sdk-for-android-explore-api-reference-latestimageformat#SVG) the bytes of a UTF-8 encoded string in SVG Tiny format are expected. For the format specification see https://www.w3.org/TR/SVGTiny12

    `imageFormat` -

    The format of the image data to be used.

    `width` -

    The width of the image in pixels.

    `height` -

    The height of the image in pixels.
- (java.lang.String,long,long)" class="section detail">

### MapImage

public MapImage(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filePath, long width, long height) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new map image from the provided path to the SVG Tiny or PNG image.

    Will throw an error if either the height or width equals zero or the path is empty.

    Trying to load a file that is not compliant with SVG Tiny or PNG results in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG specification may result in an image that exhibits unexpected artifacts.

    The caller must ensure that the file remains accessible for the entire duration of its usage by the SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that remains accessible for the entire duration of its usage by the SDK or load and pass the file content to one of the `MapImage` constructors that creates instances out of image data ([`MapImage(byte[], ImageFormat)`](#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat)), [`MapImage(byte[], ImageFormat, long, long)`](#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat,long,long))).}

    This constructor needs read storage permission to be granted.
Parameters:
    `filePath` -

    The path to image file.

    `width` -

    The width of image in pixels.

    `height` -

    The height of image in pixels.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
