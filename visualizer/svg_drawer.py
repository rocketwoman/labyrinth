from visualizer.visualizer import Visualizer

class SvgDrawer(Visualizer):
    
    def draw(self, filename, nx, ny, cell_at, treasure, wormholes):
        """Write an SVG image of the maze to filename."""

        aspect_ratio = nx / ny
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / ny, width / nx

        def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
            """Write a single wall to the SVG image file handle f."""
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width + 2 * padding, height + 2 * padding,
                          -padding, -padding, width + 2 * padding, height + 2 * padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).
            for x in range(nx):
                for y in range(ny):
                    if cell_at(x, y).walls['S']:
                        x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
                    if cell_at(x, y).walls['E']:
                        x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                        write_wall(f, x1, y1, x2, y2)
            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
            
            cell_size = height/nx
            x = (treasure.x)*cell_size+(cell_size/2)-padding+ ((cell_size-(cell_size*0.8))/2)
            y = (treasure.y)*cell_size+(cell_size/2)+5
            print('<text x="{}" y="{}" font-size="{}" text-anchor="middle" alignment-baseline="middle" >❂</text>'.\
                  format(x, y, cell_size*0.8), file=f)
            
            counter = 0
            for w in wormholes:
                counter+=1
                x = (w[0])*cell_size+(cell_size/2)-padding+ ((cell_size-(cell_size*0.8))/2)
                y = (w[1])*cell_size+(cell_size/2)+5
                print('<text x="{}" y="{}" font-size="{}" text-anchor="middle" alignment-baseline="middle" >{}</text>'.\
                  format(x, y, cell_size*0.8, counter), file=f)
            print('</svg>', file=f)