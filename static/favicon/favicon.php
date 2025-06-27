<?php
/**
 * `favicon.php` - Dynamically generate a favicon image with background color and text overlay
 * PHP Image Processing and Generation https://www.php.net/manual/en/refs.utilspec.image.php
 */

// Generate a plain black image first
$generated_image = imagecreate(32, 32);
// Set background color using RGB values
imagecolorallocate($generated_image, 0, 255, 0);  // #00FF00 Green

// Add text overlay to image. This adds a single character: `!`
// https://www.php.net/manual/en/function.imagestring.php
// To use other fonts, call `imageloadfont()` https://www.php.net/manual/en/function.imageloadfont.php
$text_color = imagecolorallocate($generated_image, 0, 0, 255); // #0000FF Blue
imagestring($generated_image, 5, 12, 8,  '!', $text_color);

// Return the actual image as a proper PNG response
header('Content-Type: image/png');
imagepng($generated_image); // Write binary data to output stream
imagedestroy($generated_image); // Ensure memory is freed
?>
