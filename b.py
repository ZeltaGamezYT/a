import math

# Chess board setup
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
pieces = ['K', 'Q', 'R', 'B', 'N', '']
modifiers = ['', '+', '#', 'x']
special_moves = ['0-0', '0-0-0']

def generate_pawn_moves():
    """Generate all possible pawn moves"""
    moves = []
    for file in files:
        for rank in ranks:
            # Basic pawn moves (no capture)
            moves.append(f"{file}{rank} (Pawn to {file}{rank})")
            
            # Pawn moves with check/checkmate
            moves.append(f"{file}{rank}+ (Pawn to {file}{rank} check)")
            moves.append(f"{file}{rank}# (Pawn to {file}{rank} checkmate)")
            
            # Pawn captures
            for target_file in files:
                if target_file != file:
                    moves.append(f"{file}x{target_file}{rank} (Pawn on {file} captures on {target_file}{rank})")
                    moves.append(f"{file}x{target_file}{rank}+ (Pawn on {file} captures on {file}{rank} check)")
                    moves.append(f"{file}x{target_file}{rank}# (Pawn on {file} captures on {file}{rank} checkmate)")
    
    return moves

def generate_piece_moves():
    """Generate moves for all pieces except pawns"""
    moves = []
    for piece in pieces:
        if piece:  # Skip empty string (pawns)
            for file in files:
                for rank in ranks:
                    # Basic piece moves
                    moves.append(f"{piece}{file}{rank} ({piece} to {file}{rank})")
                    moves.append(f"{piece}{file}{rank}+ ({piece} to {file}{rank} check)")
                    moves.append(f"{piece}{file}{rank}# ({piece} to {file}{rank} checkmate)")
                    
                    # Piece captures
                    moves.append(f"{piece}x{file}{rank} ({piece} captures on {file}{rank})")
                    moves.append(f"{piece}x{file}{rank}+ ({piece} captures on {file}{rank} check)")
                    moves.append(f"{piece}x{file}{rank}# ({piece} captures on {file}{rank} checkmate)")
                    
                    # Disambiguation moves (by file)
                    for dis_file in files:
                        if dis_file != file:
                            moves.append(f"{piece}{dis_file}{file}{rank} ({piece} on {dis_file}-file to {file}{rank})")
                            moves.append(f"{piece}{dis_file}x{file}{rank} ({piece} on {dis_file}-file captures on {file}{rank})")
                    
                    # Disambiguation moves (by rank)
                    for dis_rank in ranks:
                        if dis_rank != rank:
                            moves.append(f"{piece}{dis_rank}{file}{rank} ({piece} on {dis_rank}-rank to {file}{rank})")
                            moves.append(f"{piece}{dis_rank}x{file}{rank} ({piece} on {dis_rank}-rank captures on {file}{rank})")
    
    return moves

def generate_special_moves():
    """Generate special moves like castling"""
    moves = []
    for move in special_moves:
        moves.append(f"{move} (Kingside castling)" if move == "0-0" else f"{move} (Queenside castling)")
        moves.append(f"{move}+ (Kingside castling check)" if move == "0-0" else f"{move}+ (Queenside castling check)")
        moves.append(f"{move}# (Kingside castling checkmate)" if move == "0-0" else f"{move}# (Queenside castling checkmate)")
    return moves

def generate_promotions():
    """Generate pawn promotion moves"""
    moves = []
    for file in files:
        for promo_piece in ['Q', 'R', 'B', 'N']:
            # Promotion without capture
            moves.append(f"{file}8={promo_piece} (Pawn promotes to {promo_piece} on {file}8)")
            moves.append(f"{file}8={promo_piece}+ (Pawn promotes to {promo_piece} on {file}8 with check)")
            moves.append(f"{file}8={promo_piece}# (Pawn promotes to {promo_piece} on {file}8 with checkmate)")
            
            # Promotion with capture
            for cap_file in files:
                if cap_file != file:
                    moves.append(f"{file}x{cap_file}8={promo_piece} (Pawn on {file} captures on {cap_file}8 and promotes to {promo_piece})")
                    moves.append(f"{file}x{cap_file}8={promo_piece}+ (Pawn on {file} captures on {cap_file}8 and promotes to {promo_piece} with check)")
                    moves.append(f"{file}x{cap_file}8={promo_piece}# (Pawn on {file} captures on {cap_file}8 and promotes to {promo_piece} with checkmate)")
    return moves

def main():
    """Main function to generate chess notation"""
    print("Generating chess notation combinations...")
    
    # Generate different types of moves
    all_moves = []
    all_moves.extend(generate_pawn_moves())
    all_moves.extend(generate_piece_moves())
    all_moves.extend(generate_special_moves())
    all_moves.extend(generate_promotions())
    
    # Display a subset (first 100 moves) to avoid memory issues
    print(f"Total possible moves: {len(all_moves)}")
    print("Sample of moves:")
    for i in range(min(100, len(all_moves))):
        print(all_moves[i])
    
    # Save to file if needed (commented out due to potential size)
    # with open('chess_notation.txt', 'w') as f:
    #     for move in all_moves:
    #         f.write(move + '\n')

if __name__ == "__main__":
    main()
